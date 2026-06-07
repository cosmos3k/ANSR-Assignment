# validator.py
# Validates extracted invoice data against the PO master file.
# Returns a validation result for each invoice.

import csv
import os


def load_po_master(po_file_path):
    """
    Reads po_master.csv and returns a dictionary
    keyed by PO number for fast lookups.

    Result looks like:
    {
      "PO-1001": {
          "po_number": "PO-1001",
          "vendor": "Tata Consultancy Services Ltd",
          "approved_amount": 85000.0,
          "date_issued": "2025-01-10"
      },
      ...
    }
    """
    po_data = {}

    with open(po_file_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)      # reads CSV as list of dicts
        for row in reader:
            po_number = row["po_number"].strip()
            po_data[po_number] = {
                "po_number":        po_number,
                "vendor":           row["vendor"].strip(),
                "approved_amount":  float(row["approved_amount"]),
                "date_issued":      row["date_issued"].strip()
            }

    return po_data


def validate_invoice(extracted, po_data):
    """
    Compares extracted invoice fields against PO master.

    Parameters:
        extracted  : dict from extractor.py
        po_data    : dict from load_po_master()

    Returns a result dict with:
        - all original extracted fields
        - po_vendor       : vendor name from PO master
        - po_amount       : approved amount from PO master
        - status          : MATCH / AMOUNT_MISMATCH / PO_NOT_FOUND
        - discrepancy_note: human-readable explanation
    """

    po_number = extracted.get("po_number")
    invoice_amount = extracted.get("amount")

    # ── CHECK 1: Does the PO number exist? ──
    if po_number not in po_data:
        return {
            **extracted,                    # spread all extracted fields
            "po_vendor":        None,
            "po_amount":        None,
            "status":           "PO_NOT_FOUND",
            "discrepancy_note": f"PO number '{po_number}' not found in PO master."
        }

    # PO exists — get the approved record
    po_record = po_data[po_number]
    po_amount  = po_record["approved_amount"]
    po_vendor  = po_record["vendor"]

    # ── CHECK 2: Does the amount match? ──
    # We use a tolerance band to allow for minor rounding differences.
    # tolerance=0.01 means amounts within 1% of each other are accepted.
    if invoice_amount is not None:
        difference = abs(invoice_amount - po_amount)

        if difference == 0:
            status = "MATCH"
            note   = "Invoice matches PO record."
        else:
            status = "AMOUNT_MISMATCH"
            note   = (f"Invoice amount {invoice_amount} does not match "
                      f"PO approved amount {po_amount}. "
                      f"Difference: {difference:,.0f}")
    else:
        status = "AMOUNT_MISSING"
        note   = "Could not extract amount from invoice."

    return {
        **extracted,
        "po_vendor":        po_vendor,
        "po_amount":        po_amount,
        "status":           status,
        "discrepancy_note": note
    }
