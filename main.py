# main.py
# Entry point for the invoice automation system.
# Processes all invoices in invoices/input/ and
# updates the Excel tracker in invoices/output/

from groq import Groq
from dotenv import load_dotenv
import os
import json
from datetime import datetime
from dotenv import load_dotenv
from utils     import get_all_invoices
from extractor import extract_invoice
from validator import load_po_master, validate_invoice
from tracker   import get_or_create_tracker, append_result, save_tracker

'''
load_dotenv()
client = Groq(api_key=os.getenv('GROQ_API_KEY'))
response = client.chat.completions.create(
    model='llama-3.3-70b-versatile',
    messages=[{'role': 'user', 'content': 'Say exactly: API key works'}]
)
print(response.choices[0].message.content)
'''

# Load environment variables
load_dotenv()

# ── Configuration ──
# Uses OneDrive paths from .env if available,
# falls back to local folders for testing
INPUT_FOLDER  = os.getenv("ONEDRIVE_INPUT",  "invoices/input")
OUTPUT_FOLDER = os.getenv("ONEDRIVE_OUTPUT", "invoices/output")
ALERTS_FOLDER = os.getenv("ONEDRIVE_ALERTS", "invoices/alerts")
TRACKER_FILE  = os.path.join(OUTPUT_FOLDER, "tracker.xlsx")
PO_MASTER     = "data/po_master.csv"

def write_alert_file(result):
    """
    Writes a JSON file to the Alerts folder when a
    discrepancy is found. Power Automate watches this
    folder and sends an email when a new file appears.
    """
    os.makedirs(ALERTS_FOLDER, exist_ok=True)

    invoice_number = result.get("invoice_number") or "UNKNOWN"
    timestamp      = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename       = f"ALERT_{invoice_number}_{timestamp}.json"
    filepath       = os.path.join(ALERTS_FOLDER, filename)

    status         = result.get("status")
    vendor         = result.get("vendor", "Unknown Vendor")
    po_number      = result.get("po_number", "N/A")
    invoice_amount = result.get("amount") or 0
    po_amount      = result.get("po_amount") or 0
    note           = result.get("discrepancy_note", "")

    if status == "AMOUNT_MISMATCH":
        subject = f"Invoice Discrepancy: {invoice_number} | Amount Mismatch"
        body = (
            f"Dear {vendor},\n\n"
            f"We reviewed invoice {invoice_number} and found "
            f"an amount mismatch.\n\n"
            f"Invoice Amount : INR {invoice_amount:,}\n"
            f"PO Approved    : INR {po_amount:,}\n"
            f"PO Number      : {po_number}\n"
            f"Difference     : INR {invoice_amount - po_amount:,}\n\n"
            f"Please resubmit a corrected invoice or contact "
            f"our Finance team with supporting documentation.\n\n"
            f"Regards,\nFinance Team"
        )
    elif status == "PO_NOT_FOUND":
        subject = f"Invoice Discrepancy: {invoice_number} | PO Not Found"
        body = (
            f"Dear {vendor},\n\n"
            f"We received invoice {invoice_number} but PO number "
            f"'{po_number}' was not found in our system.\n\n"
            f"Invoice Amount : INR {invoice_amount:,}\n"
            f"PO Number      : {po_number} (NOT FOUND)\n\n"
            f"Please verify the PO number and resubmit, or contact "
            f"our Procurement team to raise a new PO.\n\n"
            f"Regards,\nFinance Team"
        )
    else:
        return None

    alert_data = {
        "vendor_email":     result.get("sender_email", ""),
        "email_subject":    subject,
        "email_body":       body,
        "invoice_number":   invoice_number,
        "vendor":           vendor,
        "status":           status,
        "discrepancy_note": note,
        "timestamp":        timestamp
    }

    with open(filepath, "w") as f:
        json.dump(alert_data, f, indent=2)

    print(f"      Alert file written: {filename}")
    return filepath


def get_sender_email(filepath):
    """
    Looks for a companion _meta.json file saved by
    Power Automate alongside the invoice file.
    Returns the sender email or empty string.

    Example:
      invoice:  Input/INV-009.docx
      metadata: Input/INV-009.docx_meta.json
                contains: {"sender_email": "billing@tcs.com"}
    """
    meta_path = filepath + "_meta.json"
    if os.path.exists(meta_path):
        try:
            with open(meta_path, "r") as f:
                meta = json.load(f)
                return meta.get("sender_email", "")
        except Exception:
            return ""
    return ""


def main():
    print("=" * 60)
    print("   INVOICE AUTOMATION SYSTEM")
    print("=" * 60)

    # Step 1: Load PO master file
    print("\n[1/4] Loading PO master file...")
    po_data = load_po_master(PO_MASTER)
    print(f"      Loaded {len(po_data)} PO records.")

    # Step 2: Scan input folder for invoice files
    print("\n[2/4] Scanning invoice folder...")
    invoice_files = get_all_invoices(INPUT_FOLDER)
    print(f"      Found {len(invoice_files)} invoice files.")

    if not invoice_files:
        print("      No invoices to process. Exiting.")
        return

    # Step 3: Prepare Excel tracker
    print("\n[3/4] Preparing Excel tracker...")
    wb, ws = get_or_create_tracker(TRACKER_FILE)

    # Step 4: Process each invoice
    print("\n[4/4] Processing invoices...\n")

    results = {
        "MATCH":           [],
        "AMOUNT_MISMATCH": [],
        "PO_NOT_FOUND":    [],
        "AMOUNT_MISSING":  [],
        "OTHER":           []
    }

    for i, filepath in enumerate(invoice_files, start=1):
        filename = os.path.basename(filepath)
        print(f"  [{i}/{len(invoice_files)}] {filename}")

        try:
            # Extract fields from invoice
            extracted = extract_invoice(filepath)
            extracted["sender_email"] = get_sender_email(filepath)

            # Validate against PO master
            result = validate_invoice(extracted, po_data)

            # Append to Excel tracker
            append_result(ws, result)

            # Track result for summary
            status = result.get("status", "OTHER")
            if status in results:
                results[status].append(filename)
            else:
                results["OTHER"].append(filename)

            # Write alert file for discrepancies
            status = result.get("status", "OTHER")
            if status in ["AMOUNT_MISMATCH", "PO_NOT_FOUND"]:
                write_alert_file(result)

            print(f"      Status: {result['status']}")
            print(f"      Note  : {result['discrepancy_note']}\n")

        except Exception as e:
            print(f"      ERROR processing {filename}: {e}\n")

    # Save the tracker
    save_tracker(wb, TRACKER_FILE)

    # Print final summary
    print("=" * 60)
    print("   SUMMARY")
    print("=" * 60)

    alerts_count = len(results['AMOUNT_MISMATCH']) + len(results['PO_NOT_FOUND'])

    print(f"  Total invoices processed : {len(invoice_files)}")
    print(f"  Matched               : {len(results['MATCH'])}")
    print(f"  Amount mismatches     : {len(results['AMOUNT_MISMATCH'])}")
    print(f"  PO not found          : {len(results['PO_NOT_FOUND'])}")
    print(f"  Other issues          : {len(results['AMOUNT_MISSING']) + len(results['OTHER'])}")
    print(f"  Alert files written   : {alerts_count}")
    print(f"\n  Input    : {INPUT_FOLDER}")
    print(f"  Tracker  : {TRACKER_FILE}")
    print(f"  Alerts   : {ALERTS_FOLDER}")
    print("=" * 60)


if __name__ == "__main__":
    main()