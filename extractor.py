# extractor.py
# Reads invoice files (PDF, DOCX, XLSX) and uses
# Groq LLM to extract structured invoice fields.

import os
import json
import fitz                          # PyMuPDF — reads PDF files
from docx import Document            # python-docx — reads DOCX files
import openpyxl                      # reads XLSX files
from groq import Groq                # Groq API client
from dotenv import load_dotenv       # loads .env file
from utils import get_file_type      # our file type detector

# Load environment variables from .env file
# This makes GROQ_API_KEY available via os.getenv()
load_dotenv()


# ─────────────────────────────────────────
# SECTION 1: FILE READERS
# Each function reads one file type and
# returns all its text as a single string
# ─────────────────────────────────────────

def read_pdf(filepath):
    """Extract all text from a PDF file."""
    text = ""
    doc = fitz.open(filepath)        # open the PDF
    for page in doc:                 # loop through every page
        text += page.get_text()      # extract text from that page
    doc.close()
    return text


def read_docx(filepath):
    """Extract all text from a DOCX file."""
    text = ""
    doc = Document(filepath)         # open the Word document
    for paragraph in doc.paragraphs: # loop through every paragraph
        text += paragraph.text + "\n"
    return text


def read_xlsx(filepath):
    """Extract all text from an XLSX file."""
    text = ""
    wb = openpyxl.load_workbook(filepath)  # open the workbook
    ws = wb.active                          # get the first sheet

    for row in ws.iter_rows():              # loop through every row
        for cell in row:                    # loop through every cell
            if cell.value is not None:      # skip empty cells
                text += str(cell.value) + "  "
        text += "\n"
    return text


def read_invoice_file(filepath):
    """
    Detects file type and routes to the correct reader.
    Returns raw text string from the invoice.
    """
    file_type = get_file_type(filepath)

    if file_type == "pdf":
        return read_pdf(filepath)
    elif file_type == "docx":
        return read_docx(filepath)
    elif file_type == "xlsx":
        return read_xlsx(filepath)
    else:
        raise ValueError(f"Unsupported file type: {filepath}")


# ─────────────────────────────────────────
# SECTION 2: LLM EXTRACTION
# Sends raw text to Groq and gets back
# structured JSON with invoice fields
# ─────────────────────────────────────────

def extract_fields_with_llm(raw_text):
    """
    Sends invoice text to Groq LLM.
    Returns a dictionary with extracted fields.
    """

    # Initialise the Groq client using the API key from .env
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    # THE PROMPT — this is what tells the LLM exactly what to do.
    # System message: sets the LLM's role and output rules.
    # User message: gives it the actual invoice text.
    system_prompt = """You are a finance data extraction assistant.
Your job is to extract specific fields from invoice text.

Always respond with ONLY a valid JSON object.
No explanation. No markdown. No code blocks. Just raw JSON.

Extract these fields:
- vendor: the company name that issued the invoice
- invoice_number: the invoice or document reference number
- date: the invoice date in YYYY-MM-DD format
- po_number: the Purchase Order number (starts with PO-)
- amount: the total amount as a number only (no currency symbols, no commas)

If a field cannot be found, use null.

Example output:
{"vendor": "ACME Corporation", "invoice_number": "INV-001", "date": "2025-06-01", "po_number": "PO-1001", "amount": 25000}"""

    user_prompt = f"""Extract the invoice fields from this text:

{raw_text}"""

    # Make the API call to Groq
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": user_prompt}
        ],
        temperature=0   # 0 = consistent, deterministic output
    )

    # Get the text response from the LLM
    response_text = response.choices[0].message.content.strip()

    # SAFE JSON PARSING
    # Sometimes LLMs wrap output in ```json ... ``` even when told not to.
    # This strips those markers if they appear.
    if response_text.startswith("```"):
        lines = response_text.split("\n")
        # Remove first line (```json) and last line (```)
        response_text = "\n".join(lines[1:-1])

    # Parse the JSON string into a Python dictionary
    extracted = json.loads(response_text)
    return extracted


# ─────────────────────────────────────────
# SECTION 3: MAIN EXTRACTION FUNCTION
# Combines reading + LLM extraction into
# one clean function call
# ─────────────────────────────────────────

def extract_invoice(filepath):
    """
    Full pipeline for one invoice file:
    1. Read the file
    2. Extract fields with LLM
    3. Add the source filename
    4. Return complete data dictionary

    Returns a dict like:
    {
        "vendor": "Tata Consultancy Services Ltd",
        "invoice_number": "INV-001",
        "date": "2025-01-25",
        "po_number": "PO-1001",
        "amount": 85000,
        "source_file": "INV-001.pdf"
    }
    """
    print(f"  Reading file: {os.path.basename(filepath)}")

    # Step 1: read raw text from file
    raw_text = read_invoice_file(filepath)

    print(f"  Sending to LLM for extraction...")

    # Step 2: send to LLM and get structured data
    extracted = extract_fields_with_llm(raw_text)

    # Step 3: add the source filename for reference
    extracted["source_file"] = os.path.basename(filepath)

    print(f"  Extracted: {extracted}")
    return extracted