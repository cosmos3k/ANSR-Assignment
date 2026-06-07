# utils.py
# Utility functions shared across the project.
# Currently handles file type detection.

import os

# Supported invoice file extensions
SUPPORTED_EXTENSIONS = [".pdf", ".docx", ".xlsx"]


def get_file_type(filepath):
    """
    Takes a file path and returns its type as a string.

    Returns:
        "pdf"  → for .pdf files
        "docx" → for .docx files
        "xlsx" → for .xlsx files
        None   → for unsupported file types
    """
    # os.path.splitext splits "invoice.pdf" into ("invoice", ".pdf")
    # [1] gives us just the extension: ".pdf"
    # .lower() makes it case-insensitive: ".PDF" becomes ".pdf"
    extension = os.path.splitext(filepath)[1].lower()

    if extension == ".pdf":
        return "pdf"
    elif extension == ".docx":
        return "docx"
    elif extension == ".xlsx":
        return "xlsx"
    else:
        return None


def get_all_invoices(input_folder):
    """
    Scans the input folder and returns a list of
    all supported invoice file paths.

    Skips hidden files (starting with .) and
    unsupported formats.
    """
    invoice_files = []

    # os.listdir returns all filenames in the folder
    for filename in os.listdir(input_folder):

        # Skip hidden files like .DS_Store on macOS
        if filename.startswith("."):
            continue

        # Build the full path: "invoices/input/INV-001.pdf"
        full_path = os.path.join(input_folder, filename)

        # Only add it if we support this file type
        if get_file_type(full_path) is not None:
            invoice_files.append(full_path)

    # Sort so files are processed in consistent order
    return sorted(invoice_files)