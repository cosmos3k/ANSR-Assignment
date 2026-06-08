# Invoice Automation System

## ANSR Internship Assignment

A typical workflow involves downloading invoice attachments from emails, extracting key information, validating the invoice against an approved Purchase Order (PO), updating tracking sheets, and communicating discrepancies back to vendors.

This project automates that workflow end-to-end using a combination of Python, LLM-powered document understanding, Microsoft Power Automate, and OneDrive.

The goal was to reduce manual effort while maintaining a clear audit trail of invoice validation decisions.

## What the System Does

The solution automatically:

* Monitors a Gmail inbox for incoming invoice emails
* Saves invoice attachments to OneDrive using Power Automate
* Extracts invoice details from PDF, DOCX, and XLSX files
* Uses Llama 3.3 (via Groq) to identify structured invoice fields
* Validates invoices against a Purchase Order master dataset
* Maintains a color-coded Excel tracker for finance teams
* Automatically sends discrepancy notifications to vendors

This creates a lightweight invoice-processing pipeline that mimics a real-world accounts payable workflow.

---

## System Architecture

The workflow consists of two automation layers:

### 1. Email Intake Layer (Power Automate)

Incoming invoice emails are automatically detected and processed.

Power Automate:

* Monitors a dedicated Gmail inbox
* Saves invoice attachments to OneDrive
* Stores vendor metadata for downstream processing

### 2. Invoice Processing Layer (Python)

The Python application processes newly received invoices and performs validation.

Processing steps:

1. Detect invoice file type
2. Extract raw text from the document
3. Use an LLM to identify invoice fields
4. Validate extracted data against PO records
5. Update the tracker workbook
6. Generate discrepancy alerts when required

### 3. Vendor Communication Layer (Power Automate)

When a discrepancy is detected:

* A JSON alert file is generated
* Power Automate monitors the Alerts folder
* A formatted email is sent back to the vendor automatically
* The alert file is archived or removed

This ensures vendors receive immediate feedback without requiring manual intervention from the finance team.
