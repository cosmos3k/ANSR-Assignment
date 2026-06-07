import os
import csv

os.makedirs("data", exist_ok=True)
os.makedirs("invoices/input", exist_ok=True)

# ─── MASTER REFERENCE DATA ────────────────────────────────────────────────────
PO_MASTER = [
    ("PO-1001", "Tata Consultancy Services Ltd", 85000, "2025-01-10"),
    ("PO-1002", "Tata Consultancy Services Ltd", 42000, "2025-02-14"),
    ("PO-1003", "Tata Consultancy Services Ltd", 67500, "2025-03-20"),
    ("PO-1004", "Infosys Technologies Pvt Ltd",  91000, "2025-01-22"),
    ("PO-1005", "Infosys Technologies Pvt Ltd",  38500, "2025-02-28"),
    ("PO-1006", "Infosys Technologies Pvt Ltd",  55000, "2025-04-05"),
    ("PO-1007", "Wipro Digital Solutions",        72000, "2025-01-15"),
    ("PO-1008", "Wipro Digital Solutions",        29500, "2025-03-11"),
    ("PO-1009", "Wipro Digital Solutions",        48000, "2025-04-18"),
    ("PO-1010", "HCL Technologies Limited",       63000, "2025-02-07"),
    ("PO-1011", "HCL Technologies Limited",       99500, "2025-03-25"),
    ("PO-1012", "HCL Technologies Limited",       17000, "2025-05-02"),
    ("PO-1013", "Mphasis Software Services",      54000, "2025-02-19"),
    ("PO-1014", "Mphasis Software Services",      78000, "2025-04-10"),
    ("PO-1015", "Mphasis Software Services",      33000, "2025-05-15"),
]

with open("data/po_master.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["po_number", "vendor", "approved_amount", "date_issued"])
    writer.writerows(PO_MASTER)
print("✓ Created: data/po_master.csv")

# inv_number, vendor, date, po_number, amount, format, result, amount_label, layout
INVOICES = [
    ("INV-001", "Tata Consultancy Services Ltd", "2025-01-25", "PO-1001", 85000,  "PDF",  "MATCH",           "Amount Due",     1),
    ("INV-002", "Tata Consultancy Services Ltd", "2025-02-28", "PO-1002", 42000,  "PDF",  "MATCH",           "Invoice Total",  2),
    ("INV-003", "Infosys Technologies Pvt Ltd",  "2025-02-10", "PO-1004", 91000,  "PDF",  "MATCH",           "Grand Total",    3),
    ("INV-004", "Infosys Technologies Pvt Ltd",  "2025-03-15", "PO-1005", 38500,  "PDF",  "MATCH",           "Balance Due",    1),
    ("INV-005", "Wipro Digital Solutions",        "2025-02-01", "PO-1007", 72000,  "PDF",  "MATCH",           "Amount Due",     2),
    ("INV-006", "Wipro Digital Solutions",        "2025-03-25", "PO-1008", 29500,  "PDF",  "MATCH",           "Net Amount",     3),
    ("INV-007", "HCL Technologies Limited",       "2025-02-20", "PO-1010", 63000,  "DOCX", "MATCH",           "Net Payable",    1),
    ("INV-008", "Mphasis Software Services",      "2025-03-05", "PO-1013", 54000,  "DOCX", "MATCH",           "Total Payable",  2),
    ("INV-009", "Tata Consultancy Services Ltd",  "2025-04-02", "PO-1003", 71000,  "DOCX", "AMOUNT_MISMATCH", "Amount Due",     3),
    ("INV-010", "Infosys Technologies Pvt Ltd",   "2025-05-10", "PO-1006", 61000,  "DOCX", "AMOUNT_MISMATCH", "Invoice Value",  1),
    ("INV-011", "HCL Technologies Limited",        "2025-04-10", "PO-1011", 95000,  "DOCX", "AMOUNT_MISMATCH", "Net Payable",   2),
    ("INV-012", "Mphasis Software Services",       "2025-05-20", "PO-1014", 82000,  "XLSX", "AMOUNT_MISMATCH", "Total Billed",  1),
    ("INV-013", "Wipro Digital Solutions",         "2025-04-22", "PO-9901", 48000,  "XLSX", "PO_NOT_FOUND",    "Grand Total",   2),
    ("INV-014", "HCL Technologies Limited",        "2025-05-05", "PO-9902", 21000,  "XLSX", "PO_NOT_FOUND",    "Invoice Total", 3),
    ("INV-015", "Mphasis Software Svc",            "2025-05-25", "PO-1015", 33000,  "XLSX", "VENDOR_MISMATCH", "Amount Due",   1),
]

VENDOR_GSTIN = {
    "Tata Consultancy Services Ltd": "27AAACT2727Q1ZW",
    "Infosys Technologies Pvt Ltd":  "29AABCI1234A1Z5",
    "Wipro Digital Solutions":        "29AABCW5678B1Z3",
    "HCL Technologies Limited":       "06AABCH9012C1Z1",
    "Mphasis Software Services":      "29AABCM3456D1Z7",
    "Mphasis Software Svc":           "29AABCM3456D1Z7",
}
VENDOR_ADDRESS = {
    "Tata Consultancy Services Ltd": "TCS House, Raveline Street, Fort, Mumbai - 400001",
    "Infosys Technologies Pvt Ltd":  "Electronics City, Hosur Road, Bengaluru - 560100",
    "Wipro Digital Solutions":        "Doddakannelli, Sarjapur Road, Bengaluru - 560035",
    "HCL Technologies Limited":       "Plot No. 3A, Sector 126, Noida - 201304",
    "Mphasis Software Services":      "Bagmane World Technology Centre, Marathahalli, Bengaluru - 560037",
    "Mphasis Software Svc":           "Bagmane World Technology Centre, Marathahalli, Bengaluru - 560037",
}
VENDOR_EMAIL = {
    "Tata Consultancy Services Ltd": "billing@tcs.com",
    "Infosys Technologies Pvt Ltd":  "accounts@infosys.com",
    "Wipro Digital Solutions":        "invoices@wipro.com",
    "HCL Technologies Limited":       "finance@hcltech.com",
    "Mphasis Software Services":      "billing@mphasis.com",
    "Mphasis Software Svc":           "billing@mphasis.com",
}
VENDOR_DESC = {
    "Tata Consultancy Services Ltd": "IT Consulting & Software Development Services",
    "Infosys Technologies Pvt Ltd":  "Enterprise Application Management & Support",
    "Wipro Digital Solutions":        "Cloud Infrastructure & DevOps Services",
    "HCL Technologies Limited":       "Digital Transformation & Analytics Services",
    "Mphasis Software Services":      "BPO & Application Outsourcing Services",
    "Mphasis Software Svc":           "BPO & Application Outsourcing Services",
}
BUYER        = "TechNova Systems Pvt Ltd"
BUYER_ADDR   = "Unit 4B, Oberoi Commerz, Off Western Express Hwy, Goregaon East, Mumbai - 400063"
BUYER_GSTIN  = "27AABCT4321E1ZK"
BUYER_EMAIL  = "accounts@technovasystems.in"

# ══════════════════════════════════════════════════════════════════════════════
#  PDF  —  3 completely different layouts
# ══════════════════════════════════════════════════════════════════════════════
from fpdf import FPDF

# ── PDF Layout 1 ──────────────────────────────────────────────────────────────
# Style: Dark navy header band, two-column meta box, classic line-items table
def pdf_layout_1(inv):
    num, vendor, date, po, amount, *_, lbl, __ = inv
    p = FPDF(); p.add_page(); p.set_margins(15,15,15)

    # Navy header
    p.set_fill_color(25,55,109); p.rect(0,0,210,28,"F")
    p.set_font("Helvetica","B",18); p.set_text_color(255,255,255)
    p.set_xy(15,6); p.cell(100,10,"TAX INVOICE")
    p.set_font("Helvetica","",9); p.set_xy(130,8)
    p.cell(65,5,"Original for Recipient",align="R")
    p.set_xy(130,14); p.cell(65,5,f"Ref: {num}",align="R")
    p.set_text_color(0,0,0)

    # Vendor (left) + meta box (right)
    p.set_xy(15,33); p.set_font("Helvetica","B",11)
    p.cell(0,6,vendor,ln=True); p.set_x(15)
    p.set_font("Helvetica","",8)
    p.multi_cell(85,4.5,VENDOR_ADDRESS[vendor]); p.set_x(15)
    p.cell(0,5,f"GSTIN: {VENDOR_GSTIN[vendor]}  |  {VENDOR_EMAIL[vendor]}",ln=True)

    p.set_fill_color(237,242,252); p.rect(112,32,83,38,"F")
    p.set_font("Helvetica","B",8)
    rows = [("Invoice No.",num),("Date",date),("PO Number",po),("Due Date","Net 30 days")]
    y=35
    for k,v in rows:
        p.set_xy(114,y); p.cell(30,5.5,k+":"); p.set_font("Helvetica","",8)
        p.cell(48,5.5,v,ln=True); p.set_font("Helvetica","B",8); y+=7.5

    # Bill To
    p.set_xy(15,78); p.set_fill_color(237,242,252)
    p.set_font("Helvetica","B",8); p.cell(180,5.5,"  Bill To",fill=True,ln=True)
    p.set_x(15); p.set_font("Helvetica","B",9); p.cell(0,5.5,BUYER,ln=True)
    p.set_x(15); p.set_font("Helvetica","",8); p.multi_cell(110,4.5,BUYER_ADDR)
    p.set_x(15); p.cell(0,5,f"GSTIN: {BUYER_GSTIN}  |  {BUYER_EMAIL}",ln=True)

    # Items table
    p.set_xy(15,115)
    p.set_fill_color(25,55,109); p.set_text_color(255,255,255)
    p.set_font("Helvetica","B",8)
    for w,h in zip([8,88,22,22,35],["Sl","Description","SAC","Unit","Amount (INR)"]):
        p.cell(w,6.5,h,align="C")
    p.ln(); p.set_text_color(0,0,0); p.set_font("Helvetica","",8)
    p.set_fill_color(249,250,253)
    for w,v in zip([8,88,22,22,35],["1",VENDOR_DESC[vendor],"998314","1 Job",f"{amount:,.0f}"]):
        p.cell(w,6.5,v,border="T",align="C",fill=True)
    p.ln()

    # Totals
    tax=round(amount*0.18); total=amount+tax
    p.set_xy(120,p.get_y()+4)
    for k,v in [("Subtotal",f"INR {amount:,.0f}"),("IGST @ 18%",f"INR {tax:,.0f}")]:
        p.set_x(120); p.set_font("Helvetica","",8)
        p.cell(40,5.5,k); p.cell(37,5.5,v,align="R",ln=True)
    p.set_x(120); p.set_fill_color(25,55,109); p.set_text_color(255,255,255)
    p.set_font("Helvetica","B",10)
    p.cell(40,8,lbl,fill=True); p.cell(37,8,f"INR {total:,.0f}",align="R",fill=True,ln=True)
    p.set_text_color(0,0,0)

    p.set_xy(15,252); p.set_font("Helvetica","I",7.5); p.set_text_color(120,120,120)
    p.cell(0,5,f"Computer-generated invoice. PO Ref: {po}. Payment due within 30 days.",ln=True)
    return p

# ── PDF Layout 2 ──────────────────────────────────────────────────────────────
# Style: Minimalist — no header band; left-aligned vendor block, right-side invoice
#        meta as a bordered card, muted grey totals
def pdf_layout_2(inv):
    num, vendor, date, po, amount, *_, lbl, __ = inv
    p = FPDF(); p.add_page(); p.set_margins(20,20,20)
    p.set_text_color(0,0,0)

    # Top rule
    p.set_draw_color(200,200,200); p.set_line_width(0.8)
    p.line(20,18,190,18)

    # Vendor (left)
    p.set_xy(20,22); p.set_font("Helvetica","B",13); p.set_text_color(40,40,40)
    p.cell(0,7,vendor,ln=True)
    p.set_x(20); p.set_font("Helvetica","",8); p.set_text_color(90,90,90)
    p.multi_cell(90,4.5,VENDOR_ADDRESS[vendor])
    p.set_x(20); p.cell(0,4.5,f"GSTIN: {VENDOR_GSTIN[vendor]}",ln=True)
    p.set_x(20); p.cell(0,4.5,VENDOR_EMAIL[vendor],ln=True)

    # Invoice card (right) — drawn manually
    p.set_draw_color(180,180,180); p.set_line_width(0.3)
    p.rect(120,20,68,40)
    p.set_fill_color(245,245,245); p.rect(120,20,68,7,"F")
    p.set_xy(121,22); p.set_font("Helvetica","B",9); p.set_text_color(40,40,40)
    p.cell(66,4,"INVOICE DETAILS",align="C",ln=True)
    card_rows=[("Invoice #",num),("Date",date),("PO #",po),("Payment","Net 30")]
    y=28
    for k,v in card_rows:
        p.set_xy(122,y); p.set_font("Helvetica","B",8); p.cell(22,5,k+":")
        p.set_font("Helvetica","",8); p.cell(42,5,v,ln=True); y+=6

    # Bill To
    p.set_xy(20,72); p.set_font("Helvetica","B",8); p.set_text_color(90,90,90)
    p.cell(0,5,"BILL TO",ln=True)
    p.set_x(20); p.set_font("Helvetica","B",10); p.set_text_color(20,20,20)
    p.cell(0,5.5,BUYER,ln=True)
    p.set_x(20); p.set_font("Helvetica","",8); p.set_text_color(80,80,80)
    p.multi_cell(110,4.5,BUYER_ADDR)
    p.set_x(20); p.cell(0,4.5,f"GSTIN: {BUYER_GSTIN}",ln=True)

    p.line(20,110,190,110)

    # Items
    p.set_xy(20,114); p.set_font("Helvetica","B",8); p.set_text_color(40,40,40)
    for w,h in zip([8,94,20,22,26],["No.","Service / Description","SAC","Qty","Amount"]):
        p.cell(w,5.5,h)
    p.ln()
    p.set_draw_color(180,180,180); p.line(20,120,190,120)
    p.set_font("Helvetica","",8); p.set_text_color(60,60,60)
    for w,v in zip([8,94,20,22,26],["1",VENDOR_DESC[vendor],"998314","1",f"{amount:,.0f}"]):
        p.cell(w,6,v)
    p.ln()
    p.line(20,127,190,127)

    # Totals — right-aligned block
    tax=round(amount*0.18); total=amount+tax
    p.set_font("Helvetica","",8); p.set_text_color(70,70,70)
    for k,v in [("Sub-Total",f"{amount:,.0f}"),("IGST 18%",f"{tax:,.0f}")]:
        p.set_xy(140,p.get_y()+2); p.cell(28,5.5,k); p.cell(22,5.5,f"INR {v}",align="R",ln=True)
    p.set_xy(140,p.get_y()+1)
    p.set_fill_color(230,230,230); p.set_text_color(20,20,20)
    p.set_font("Helvetica","B",9)
    p.cell(28,7,lbl,fill=True); p.cell(22,7,f"INR {total:,.0f}",align="R",fill=True,ln=True)
    p.set_text_color(0,0,0)

    # Bank details box
    p.set_xy(20,175); p.set_fill_color(248,248,248); p.rect(20,175,100,30,"F")
    p.set_xy(22,177); p.set_font("Helvetica","B",8); p.cell(0,5,"Payment Details",ln=True)
    p.set_font("Helvetica","",7.5); p.set_text_color(70,70,70)
    for line in ["Bank: HDFC Bank Ltd","A/C No: 50200012345678","IFSC: HDFC0001234","Branch: Mumbai - Fort"]:
        p.set_x(22); p.cell(0,4.5,line,ln=True)

    p.set_xy(20,252); p.set_font("Helvetica","I",7); p.set_text_color(150,150,150)
    p.cell(0,5,f"This is a system generated document. PO: {po}. No physical signature required.")
    return p

# ── PDF Layout 3 ──────────────────────────────────────────────────────────────
# Style: Teal accent bar on left side, invoice number large on top-right,
#        stacked blocks (vendor → buyer → items → totals), no header band
def pdf_layout_3(inv):
    num, vendor, date, po, amount, *_, lbl, __ = inv
    p = FPDF(); p.add_page(); p.set_margins(22,15,15)

    # Left accent bar
    p.set_fill_color(0,150,136); p.rect(0,0,8,297,"F")

    # Invoice number large (top right)
    p.set_xy(120,12); p.set_font("Helvetica","B",22); p.set_text_color(0,150,136)
    p.cell(75,10,"INVOICE",align="R",ln=True)
    p.set_xy(120,22); p.set_font("Helvetica","",9); p.set_text_color(80,80,80)
    p.cell(75,5,num,align="R",ln=True)
    p.set_xy(120,28); p.cell(75,5,f"Date: {date}",align="R",ln=True)

    # Vendor block
    p.set_xy(22,14); p.set_font("Helvetica","B",12); p.set_text_color(20,20,20)
    p.cell(90,6,vendor,ln=True)
    p.set_x(22); p.set_font("Helvetica","",8); p.set_text_color(80,80,80)
    p.multi_cell(90,4,VENDOR_ADDRESS[vendor])
    p.set_x(22); p.set_font("Helvetica","",8)
    p.cell(0,4.5,f"GSTIN: {VENDOR_GSTIN[vendor]}",ln=True)

    # Divider
    p.set_draw_color(0,150,136); p.set_line_width(0.5); p.line(22,55,195,55)

    # Two-column info block
    p.set_xy(22,60); p.set_font("Helvetica","B",8); p.set_text_color(0,150,136)
    p.cell(85,5,"BILLED TO"); p.set_x(120); p.cell(75,5,"PURCHASE ORDER",ln=True)
    p.set_x(22); p.set_font("Helvetica","B",9); p.set_text_color(20,20,20)
    p.cell(85,5,BUYER); p.set_x(120); p.set_font("Helvetica","",9)
    p.cell(75,5,po,ln=True)
    p.set_x(22); p.set_font("Helvetica","",8); p.set_text_color(80,80,80)
    p.multi_cell(85,4,BUYER_ADDR)
    y_after=p.get_y()
    p.set_xy(120,75); p.cell(0,4.5,f"GSTIN: {BUYER_GSTIN}",ln=True)
    p.set_xy(120,80); p.cell(0,4.5,f"Due: Net 30 days",ln=True)

    p.set_y(max(y_after,88)+4)
    p.line(22,p.get_y(),195,p.get_y())

    # Items header (teal bg)
    y0=p.get_y()+2; p.set_fill_color(0,150,136); p.set_text_color(255,255,255)
    p.set_font("Helvetica","B",8)
    p.set_xy(22,y0)
    for w,h in zip([7,90,20,22,34],["#","Description of Services","SAC","Qty","Amount (INR)"]):
        p.cell(w,6,h,align="C",fill=True)
    p.ln()
    p.set_text_color(40,40,40); p.set_font("Helvetica","",8)
    p.set_fill_color(240,253,252)
    for w,v in zip([7,90,20,22,34],["1",VENDOR_DESC[vendor],"998314","1 Job",f"{amount:,.0f}"]):
        p.cell(w,6,v,align="C",fill=True)
    p.ln()
    p.line(22,p.get_y(),195,p.get_y())

    # Totals
    tax=round(amount*0.18); total=amount+tax
    ty=p.get_y()+4
    for k,v in [("Subtotal",f"INR {amount:,.0f}"),("IGST @ 18%",f"INR {tax:,.0f}")]:
        p.set_xy(130,ty); p.set_font("Helvetica","",8); p.set_text_color(70,70,70)
        p.cell(32,5.5,k); p.cell(32,5.5,f"{v}",align="R",ln=True); ty+=6
    p.set_xy(130,ty)
    p.set_fill_color(0,150,136); p.set_text_color(255,255,255)
    p.set_font("Helvetica","B",10)
    p.cell(32,8,lbl,fill=True); p.cell(32,8,f"INR {total:,.0f}",align="R",fill=True,ln=True)
    p.set_text_color(0,0,0)

    # Notes
    p.set_xy(22,p.get_y()+8); p.set_font("Helvetica","B",8); p.set_text_color(0,150,136)
    p.cell(0,5,"Notes & Terms",ln=True)
    p.set_x(22); p.set_font("Helvetica","",7.5); p.set_text_color(90,90,90)
    p.multi_cell(100,4,"1. Payment due within 30 days.\n2. Late payments subject to 1.5% monthly interest.\n3. All disputes subject to Mumbai jurisdiction.")

    p.set_xy(22,252); p.set_font("Helvetica","I",7); p.set_text_color(160,160,160)
    p.cell(0,5,f"Computer-generated tax invoice. GSTIN: {VENDOR_GSTIN[vendor]}  |  PO Ref: {po}")
    return p

def draw_pdf(inv):
    layout = inv[8]
    fn = {1: pdf_layout_1, 2: pdf_layout_2, 3: pdf_layout_3}[layout]
    pdf = fn(inv)
    path = f"invoices/input/{inv[0]}.pdf"
    pdf.output(path)
    print(f"  ✓ PDF (layout {layout}): {path}")

for inv in INVOICES:
    if inv[5] == "PDF":
        draw_pdf(inv)

# ══════════════════════════════════════════════════════════════════════════════
#  DOCX  —  3 completely different layouts
# ══════════════════════════════════════════════════════════════════════════════
from docx import Document
from docx.shared import Pt, RGBColor, Inches, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

def _shd(cell, hex_color):
    tc = cell._tc; tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"),"clear"); shd.set(qn("w:color"),"auto")
    shd.set(qn("w:fill"),hex_color); tcPr.append(shd)

def _run(para, text, bold=False, size=10, color=None, italic=False):
    r = para.add_run(text); r.bold=bold; r.italic=italic
    r.font.size=Pt(size)
    if color: r.font.color.rgb=RGBColor(*color)
    return r

def _para(doc, text="", bold=False, size=10, align="left", color=None, space_after=2):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.space_before = Pt(0)
    align_map={"left":WD_ALIGN_PARAGRAPH.LEFT,"center":WD_ALIGN_PARAGRAPH.CENTER,"right":WD_ALIGN_PARAGRAPH.RIGHT}
    p.alignment = align_map.get(align, WD_ALIGN_PARAGRAPH.LEFT)
    if text: _run(p,text,bold,size,color)
    return p

def _margins(doc, cm_val=1.8):
    for s in doc.sections:
        s.top_margin=s.bottom_margin=s.left_margin=s.right_margin=Cm(cm_val)

# ── DOCX Layout 1 ──────────────────────────────────────────────────────────────
# Style: Centered header with vendor name, two-column meta table, bordered items,
#        right-aligned totals table. Classic corporate style.
def docx_layout_1(inv):
    num, vendor, date, po, amount, *_, lbl, __ = inv
    doc = Document(); _margins(doc)

    _para(doc,vendor,bold=True,size=15,align="center",color=(25,55,109),space_after=1)
    _para(doc,VENDOR_ADDRESS[vendor],size=8,align="center",color=(80,80,80),space_after=1)
    _para(doc,f"GSTIN: {VENDOR_GSTIN[vendor]}",size=8,align="center",color=(80,80,80),space_after=1)
    _para(doc,"TAX INVOICE",bold=True,size=13,align="center",color=(25,55,109))
    _para(doc)

    # 2-col meta table
    mt = doc.add_table(rows=3,cols=4); mt.style="Table Grid"
    rows_data=[
        ("Invoice Number",num,"Invoice Date",date),
        ("PO Reference",po,"Payment Terms","Net 30 Days"),
        ("Bill To",BUYER,"Buyer GSTIN",BUYER_GSTIN),
    ]
    for ri,rd in enumerate(rows_data):
        row=mt.rows[ri]
        for ci,txt in enumerate(rd):
            cell=row.cells[ci]; p=cell.paragraphs[0]
            r=p.add_run(txt); r.bold=(ci%2==0); r.font.size=Pt(8.5)
            if ci%2==0: _shd(cell,"D9E1F2")
    _para(doc)

    # Items table
    it = doc.add_table(rows=2,cols=4); it.style="Table Grid"
    for ci,h in enumerate(["#","Description of Services","SAC Code","Amount (INR)"]):
        cell=it.rows[0].cells[ci]; _shd(cell,"19376D"); p=cell.paragraphs[0]
        r=p.add_run(h); r.bold=True; r.font.size=Pt(8.5); r.font.color.rgb=RGBColor(255,255,255)
        p.alignment=WD_ALIGN_PARAGRAPH.CENTER
    for ci,v in enumerate(["1",VENDOR_DESC[vendor],"998314",f"{amount:,.0f}"]):
        cell=it.rows[1].cells[ci]; p=cell.paragraphs[0]
        p.add_run(v).font.size=Pt(8.5); p.alignment=WD_ALIGN_PARAGRAPH.CENTER
    _para(doc)

    # Totals table
    tax=round(amount*0.18); total=amount+tax
    tt = doc.add_table(rows=3,cols=2); tt.style="Table Grid"
    for ri,(k,v) in enumerate([("Subtotal",f"INR {amount:,.0f}"),
                                 ("IGST @ 18%",f"INR {tax:,.0f}"),
                                 (lbl,f"INR {total:,.0f}")]):
        lc=tt.rows[ri].cells[0]; rc=tt.rows[ri].cells[1]
        lp=lc.paragraphs[0]; rp=rc.paragraphs[0]
        rp.alignment=WD_ALIGN_PARAGRAPH.RIGHT
        if ri==2:
            _shd(lc,"19376D"); _shd(rc,"19376D")
            for p2,t2 in [(lp,k),(rp,v)]:
                r=p2.add_run(t2); r.bold=True; r.font.size=Pt(10); r.font.color.rgb=RGBColor(255,255,255)
        else:
            lp.add_run(k).font.size=Pt(8.5); rp.add_run(v).font.size=Pt(8.5)
    _para(doc)
    ft=_para(doc,f"PO Ref: {po}  |  Payment within 30 days  |  GSTIN: {VENDOR_GSTIN[vendor]}",
             size=7.5,align="center",color=(130,130,130))
    return doc

# ── DOCX Layout 2 ──────────────────────────────────────────────────────────────
# Style: Left-aligned vendor block, invoice meta as a bordered side card using a
#        1x2 table for side-by-side vendor/meta, itemised table with grey stripes.
def docx_layout_2(inv):
    num, vendor, date, po, amount, *_, lbl, __ = inv
    doc = Document(); _margins(doc)

    # Side-by-side: vendor left, meta right
    top = doc.add_table(rows=1,cols=2); top.style="Table Grid"
    lc=top.rows[0].cells[0]; rc=top.rows[0].cells[1]
    _shd(lc,"F0F4FB"); _shd(rc,"FAFAFA")
    lp=lc.paragraphs[0]
    _run(lp,vendor+"\n",bold=True,size=12,color=(30,30,100))
    _run(lp,VENDOR_ADDRESS[vendor]+"\n",size=8,color=(80,80,80))
    _run(lp,f"GSTIN: {VENDOR_GSTIN[vendor]}\n",size=8,color=(80,80,80))
    _run(lp,VENDOR_EMAIL[vendor],size=8,color=(80,80,80))

    rp=rc.paragraphs[0]
    _run(rp,"INVOICE\n",bold=True,size=14,color=(30,30,100))
    for k,v in [("Number",num),("Date",date),("PO",po),("Terms","30 Days Net")]:
        _run(rp,f"{k}: ",bold=True,size=8.5,color=(50,50,50))
        _run(rp,v+"\n",size=8.5,color=(50,50,50))
    rp.alignment=WD_ALIGN_PARAGRAPH.RIGHT
    _para(doc)

    # Bill To
    bt=doc.add_table(rows=1,cols=1); bt.style="Table Grid"
    _shd(bt.rows[0].cells[0],"EEF2FA")
    bp=bt.rows[0].cells[0].paragraphs[0]
    _run(bp,"Bill To: ",bold=True,size=9,color=(30,30,100))
    _run(bp,f"{BUYER}  |  {BUYER_ADDR}  |  GSTIN: {BUYER_GSTIN}",size=8.5)
    _para(doc)

    # Items with striped rows
    it=doc.add_table(rows=3,cols=5); it.style="Table Grid"
    hdrs=["Sl#","Description","HSN/SAC","Quantity","Payable (INR)"]
    for ci,h in enumerate(hdrs):
        cell=it.rows[0].cells[ci]; _shd(cell,"2E4A7D"); p=cell.paragraphs[0]
        r=p.add_run(h); r.bold=True; r.font.size=Pt(8.5); r.font.color.rgb=RGBColor(255,255,255)
        p.alignment=WD_ALIGN_PARAGRAPH.CENTER
    for ci,v in enumerate(["1",VENDOR_DESC[vendor],"998314","1 Unit",f"{amount:,.0f}"]):
        cell=it.rows[1].cells[ci]; _shd(cell,"F5F7FC"); p=cell.paragraphs[0]
        p.add_run(v).font.size=Pt(8.5); p.alignment=WD_ALIGN_PARAGRAPH.CENTER
    # Sub-total row
    _shd(it.rows[2].cells[0],"FFFFFF")
    tax=round(amount*0.18); total=amount+tax
    for ci in range(5):
        cell=it.rows[2].cells[ci]; _shd(cell,"FFFFFF")
    sc=it.rows[2].cells[3]; sp=sc.paragraphs[0]
    sp.add_run("Subtotal").font.size=Pt(8.5); sp.alignment=WD_ALIGN_PARAGRAPH.RIGHT
    vc=it.rows[2].cells[4]; vp=vc.paragraphs[0]
    vp.add_run(f"{amount:,.0f}").font.size=Pt(8.5); vp.alignment=WD_ALIGN_PARAGRAPH.CENTER
    _para(doc)

    # Totals right-float via 3-row table
    tt=doc.add_table(rows=3,cols=2); tt.style="Table Grid"
    for ri,(k,v) in enumerate([("IGST @ 18%",f"INR {tax:,.0f}"),
                                 ("Round Off","INR 0.00"),
                                 (lbl,f"INR {total:,.0f}")]):
        lc2=tt.rows[ri].cells[0]; rc2=tt.rows[ri].cells[1]
        lp2=lc2.paragraphs[0]; rp2=rc2.paragraphs[0]
        rp2.alignment=WD_ALIGN_PARAGRAPH.RIGHT
        if ri==2:
            _shd(lc2,"2E4A7D"); _shd(rc2,"2E4A7D")
            for p2,t2 in [(lp2,k),(rp2,v)]:
                r=p2.add_run(t2); r.bold=True; r.font.size=Pt(10); r.font.color.rgb=RGBColor(255,255,255)
        else:
            lp2.add_run(k).font.size=Pt(8.5); rp2.add_run(v).font.size=Pt(8.5)
    _para(doc)
    _para(doc,f"Generated by {vendor} automated billing system  |  PO: {po}",
          size=7.5,align="center",color=(150,150,150))
    return doc

# ── DOCX Layout 3 ──────────────────────────────────────────────────────────────
# Style: Bold teal company name top-left, invoice metadata as a 2-col "card" 
#        on the right, items in a 3-column compact table, totals inline.
def docx_layout_3(inv):
    num, vendor, date, po, amount, *_, lbl, __ = inv
    doc = Document(); _margins(doc)

    # Teal title bar as a 1-row table
    bar=doc.add_table(rows=1,cols=1); bar.style="Table Grid"
    _shd(bar.rows[0].cells[0],"00897B")
    bp=bar.rows[0].cells[0].paragraphs[0]
    _run(bp,"TAX INVOICE",bold=True,size=16,color=(255,255,255))
    bp.alignment=WD_ALIGN_PARAGRAPH.CENTER
    _para(doc)

    # 2-col top block
    top=doc.add_table(rows=1,cols=2); top.style="Table Grid"
    lc=top.rows[0].cells[0]; rc=top.rows[0].cells[1]
    _shd(lc,"E8F5F3"); _shd(rc,"F9F9F9")
    lp=lc.paragraphs[0]
    _run(lp,vendor+"\n",bold=True,size=11,color=(0,105,92))
    _run(lp,VENDOR_ADDRESS[vendor]+"\n",size=8,color=(80,80,80))
    _run(lp,f"GSTIN: {VENDOR_GSTIN[vendor]}\n",size=8)
    _run(lp,f"Email: {VENDOR_EMAIL[vendor]}",size=8)

    rp=rc.paragraphs[0]; rp.alignment=WD_ALIGN_PARAGRAPH.RIGHT
    for k,v in [("Invoice No.",num),("Invoice Date",date),
                ("Purchase Order",po),("Payment Terms","Net 30 Days")]:
        _run(rp,f"{k}:  ",bold=True,size=8.5,color=(0,105,92))
        _run(rp,v+"  \n",size=8.5)
    _para(doc)

    # Bill To as single row table
    bt=doc.add_table(rows=1,cols=1); bt.style="Table Grid"
    _shd(bt.rows[0].cells[0],"E0F2F1")
    bp2=bt.rows[0].cells[0].paragraphs[0]
    _run(bp2,"Recipient:  ",bold=True,size=9,color=(0,105,92))
    _run(bp2,f"{BUYER}   {BUYER_ADDR}   GSTIN: {BUYER_GSTIN}",size=8.5)
    _para(doc)

    # Items table — compact 4 cols
    it=doc.add_table(rows=2,cols=4); it.style="Table Grid"
    for ci,h in enumerate(["#","Particulars / Description","SAC","Value (INR)"]):
        cell=it.rows[0].cells[ci]; _shd(cell,"00897B"); p=cell.paragraphs[0]
        r=p.add_run(h); r.bold=True; r.font.size=Pt(9); r.font.color.rgb=RGBColor(255,255,255)
        p.alignment=WD_ALIGN_PARAGRAPH.CENTER
    for ci,v in enumerate(["1",VENDOR_DESC[vendor],"998314",f"{amount:,.0f}"]):
        cell=it.rows[1].cells[ci]; _shd(cell,"F0FBF9"); p=cell.paragraphs[0]
        p.add_run(v).font.size=Pt(8.5); p.alignment=WD_ALIGN_PARAGRAPH.CENTER
    _para(doc)

    # Totals
    tax=round(amount*0.18); total=amount+tax
    tt=doc.add_table(rows=3,cols=2); tt.style="Table Grid"
    for ri,(k,v) in enumerate([("Sub Total",f"INR {amount:,.0f}"),
                                 ("Add: IGST @ 18%",f"INR {tax:,.0f}"),
                                 (lbl,f"INR {total:,.0f}")]):
        lc2=tt.rows[ri].cells[0]; rc2=tt.rows[ri].cells[1]
        lp2=lc2.paragraphs[0]; rp2=rc2.paragraphs[0]
        rp2.alignment=WD_ALIGN_PARAGRAPH.RIGHT
        if ri==2:
            _shd(lc2,"00897B"); _shd(rc2,"00897B")
            for p2,t2 in [(lp2,k),(rp2,v)]:
                r=p2.add_run(t2); r.bold=True; r.font.size=Pt(10); r.font.color.rgb=RGBColor(255,255,255)
        else:
            lp2.add_run(k).font.size=Pt(8.5); rp2.add_run(v).font.size=Pt(8.5)
    _para(doc)

    # Signature + notes row
    sn=doc.add_table(rows=1,cols=2); sn.style="Table Grid"
    _shd(sn.rows[0].cells[0],"F9F9F9"); _shd(sn.rows[0].cells[1],"F9F9F9")
    np2=sn.rows[0].cells[0].paragraphs[0]
    _run(np2,"Terms: ",bold=True,size=8); _run(np2,"Payment within 30 days. Subject to Mumbai jurisdiction.",size=8)
    sp2=sn.rows[0].cells[1].paragraphs[0]
    _run(sp2,"Authorised Signatory\n\n",bold=True,size=8); _run(sp2,vendor,size=7.5,color=(100,100,100))
    sp2.alignment=WD_ALIGN_PARAGRAPH.CENTER
    return doc

def draw_docx(inv):
    layout=inv[8]
    fn={1:docx_layout_1,2:docx_layout_2,3:docx_layout_3}[layout]
    doc=fn(inv)
    path=f"invoices/input/{inv[0]}.docx"
    doc.save(path)
    print(f"  ✓ DOCX (layout {layout}): {path}")

for inv in INVOICES:
    if inv[5]=="DOCX":
        draw_docx(inv)

# ══════════════════════════════════════════════════════════════════════════════
#  XLSX  —  3 completely different layouts
# ══════════════════════════════════════════════════════════════════════════════
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

def _fill(hex_color):
    return PatternFill("solid", fgColor=hex_color)
def _font(bold=False,size=10,color="000000",italic=False):
    return Font(bold=bold,size=size,color=color,italic=italic,name="Calibri")
def _align(h="left",v="center",wrap=False):
    return Alignment(horizontal=h,vertical=v,wrap_text=wrap)
def _border(color="CCCCCC",style="thin"):
    s=Side(style=style,color=color)
    return Border(left=s,right=s,top=s,bottom=s)

def xc(ws,ref,val,bold=False,size=10,bg=None,ha="left",fc="000000",
        bdr=False,italic=False,wrap=False):
    c=ws[ref]; c.value=val
    c.font=_font(bold,size,fc,italic)
    c.alignment=_align(ha,"center",wrap)
    if bg: c.fill=_fill(bg)
    if bdr: c.border=_border()
    return c

# ── XLSX Layout 1 ──────────────────────────────────────────────────────────────
# Style: Navy header spanning full width, two-row meta section, structured items
#        table, totals on the right. Dense, corporate spreadsheet look.
def xlsx_layout_1(inv):
    num, vendor, date, po, amount, *_, lbl, __ = inv
    wb=Workbook(); ws=wb.active; ws.title="Tax Invoice"
    for col,w in zip("ABCDEF",[5,26,18,18,18,20]):
        ws.column_dimensions[col].width=w
    for r,h in {1:6,2:32,3:18,4:6,5:14,6:14,7:14,8:14,9:6,10:16,11:16,12:6,
                13:18,14:18,15:18,16:18,17:6,18:18,19:14,20:14}.items():
        ws.row_dimensions[r].height=h

    ws.merge_cells("B2:F2")
    xc(ws,"B2",vendor,bold=True,size=15,bg="19376D",ha="center",fc="FFFFFF")
    ws.merge_cells("B3:F3")
    xc(ws,"B3",f"{VENDOR_ADDRESS[vendor]}  |  GSTIN: {VENDOR_GSTIN[vendor]}",
       size=8,bg="19376D",ha="center",fc="B0C4DE",wrap=True)

    ws.merge_cells("B5:C5"); xc(ws,"B5","TAX INVOICE",bold=True,size=12,bg="D9E1F2",ha="center")
    ws.merge_cells("D5:F5"); xc(ws,"D5","Original for Recipient",size=8,bg="D9E1F2",ha="right",fc="555555")

    meta=[("B6","Invoice Number","C6",num),("D6","Invoice Date","E6",date),
          ("B7","PO Reference","C7",po),("D7","Payment Terms","E7","Net 30 Days"),
          ("B8","GSTIN (Vendor)","C8",VENDOR_GSTIN[vendor]),("D8","Email","E8",VENDOR_EMAIL[vendor])]
    for lr,lv,vr,vv in meta:
        xc(ws,lr,lv,bold=True,size=8.5,bg="EEF2FA",bdr=True)
        xc(ws,vr,vv,size=8.5,bdr=True)

    ws.merge_cells("B10:C10"); xc(ws,"B10","Bill To",bold=True,size=9,bg="EEF2FA",bdr=True)
    ws.merge_cells("D10:F10"); xc(ws,"D10",BUYER,bold=True,size=9,bdr=True)
    ws.merge_cells("B11:C11"); xc(ws,"B11","Address",bold=True,size=8.5,bg="EEF2FA",bdr=True)
    ws.merge_cells("D11:F11"); xc(ws,"D11",BUYER_ADDR,size=8,bdr=True,wrap=True)
    ws.merge_cells("B12:C12"); xc(ws,"B12","Buyer GSTIN",bold=True,size=8.5,bg="EEF2FA",bdr=True)
    ws.merge_cells("D12:F12"); xc(ws,"D12",BUYER_GSTIN,size=8.5,bdr=True)

    for ci,(h,col) in enumerate(zip(["#","Description","SAC Code","Quantity",lbl],"BCDEF")):
        xc(ws,f"{col}14",h,bold=True,size=9,bg="19376D",ha="center",fc="FFFFFF",bdr=True)
    for ci,(v,col) in enumerate(zip(["1",VENDOR_DESC[vendor],"998314","1 Job",f"{amount:,.0f}"],"BCDEF")):
        xc(ws,f"{col}15",v,size=9,bg="F4F6FB",ha="center",bdr=True)

    tax=round(amount*0.18); total=amount+tax
    ws.merge_cells("B17:D17"); xc(ws,"B17","Subtotal",bold=False,size=9,bdr=True)
    ws.merge_cells("E17:F17"); xc(ws,"E17",f"INR {amount:,.0f}",size=9,ha="right",bdr=True)
    ws.merge_cells("B18:D18"); xc(ws,"B18","IGST @ 18%",size=9,bdr=True)
    ws.merge_cells("E18:F18"); xc(ws,"E18",f"INR {tax:,.0f}",size=9,ha="right",bdr=True)
    ws.merge_cells("B19:D19"); xc(ws,"B19",lbl,bold=True,size=11,bg="19376D",fc="FFFFFF",bdr=True)
    ws.merge_cells("E19:F19"); xc(ws,"E19",f"INR {total:,.0f}",bold=True,size=11,bg="19376D",fc="FFFFFF",ha="right",bdr=True)

    ws.merge_cells("B21:F21")
    xc(ws,"B21",f"PO Reference: {po}  |  Payment due within 30 days  |  Subject to Mumbai jurisdiction",
       size=7.5,italic=True,fc="888888",ha="center")
    return wb

# ── XLSX Layout 2 ──────────────────────────────────────────────────────────────
# Style: Minimal white background, teal accent colour, invoice number large
#        in top-right, vendor and buyer stacked left, items table with no fill,
#        only borders. Looks like a modern SaaS-generated invoice.
def xlsx_layout_2(inv):
    num, vendor, date, po, amount, *_, lbl, __ = inv
    wb=Workbook(); ws=wb.active; ws.title="Invoice"
    for col,w in zip("ABCDEFG",[3,28,18,16,16,16,18]):
        ws.column_dimensions[col].width=w
    for r,h in {1:8,2:28,3:16,4:10,5:14,6:14,7:8,8:14,9:14,10:14,11:8,
                12:18,13:16,14:8,15:18,16:14,17:14,18:14,19:14}.items():
        ws.row_dimensions[r].height=h

    # Large invoice number top-right
    ws.merge_cells("E2:G2")
    xc(ws,"E2","INVOICE",bold=True,size=18,ha="right",fc="009688")
    ws.merge_cells("E3:G3")
    xc(ws,"E3",num,bold=True,size=11,ha="right",fc="555555")

    # Vendor top-left
    ws.merge_cells("B2:D2")
    xc(ws,"B2",vendor,bold=True,size=12,fc="222222")
    ws.merge_cells("B3:D3")
    xc(ws,"B3",VENDOR_ADDRESS[vendor],size=8,fc="666666",wrap=True)
    ws.merge_cells("B4:D4")  # blank spacer row already handled
    ws.merge_cells("B5:D5")
    xc(ws,"B5",f"GSTIN: {VENDOR_GSTIN[vendor]}",size=8,fc="666666")
    ws.merge_cells("B6:D6")
    xc(ws,"B6",VENDOR_EMAIL[vendor],size=8,fc="009688")

    # Invoice details card
    for lr,lv,vr,vv in [("E5","Date","F5",date),("E6","PO No.","F6",po),("E7","Due","F7","Net 30")]:
        xc(ws,lr,lv,bold=True,size=8.5,fc="009688")
        xc(ws,vr,vv,size=8.5)

    # Divider — top border of row 8
    ws.merge_cells("B8:G8")
    c=ws["B8"]; c.border=Border(top=Side(style="medium",color="009688"))

    # Bill To
    ws.merge_cells("B9:C9"); xc(ws,"B9","BILLED TO",bold=True,size=8,fc="009688")
    ws.merge_cells("B10:D10"); xc(ws,"B10",BUYER,bold=True,size=10)
    ws.merge_cells("B11:G11"); xc(ws,"B11",BUYER_ADDR,size=8,fc="666666",wrap=True)
    ws.merge_cells("B12:D12"); xc(ws,"B12",f"GSTIN: {BUYER_GSTIN}",size=8,fc="666666")

    # Items header
    for ci,(h,col) in enumerate(zip(["No.","Service Description","SAC","Qty",lbl],"BCDFG")):
        xc(ws,f"{col}14",h,bold=True,size=9,bdr=True,ha="center",
           bg="E0F2F1",fc="004D40")
    for ci,(v,col) in enumerate(zip(["1",VENDOR_DESC[vendor],"998314","1",f"{amount:,.0f}"],"BCDFG")):
        xc(ws,f"{col}15",v,size=9,bdr=True,ha="center")

    tax=round(amount*0.18); total=amount+tax
    xc(ws,"F17","Sub-Total",bold=False,size=8.5,ha="right"); xc(ws,"G17",f"INR {amount:,.0f}",size=8.5,ha="right")
    xc(ws,"F18","IGST 18%",bold=False,size=8.5,ha="right"); xc(ws,"G18",f"INR {tax:,.0f}",size=8.5,ha="right")
    xc(ws,"F19",lbl,bold=True,size=10,bg="009688",fc="FFFFFF",ha="right",bdr=True)
    xc(ws,"G19",f"INR {total:,.0f}",bold=True,size=10,bg="009688",fc="FFFFFF",ha="right",bdr=True)

    ws.merge_cells("B21:G21")
    xc(ws,"B21",f"All disputes subject to Mumbai jurisdiction. PO Ref: {po}.",
       size=7.5,italic=True,fc="AAAAAA",ha="center")
    return wb

# ── XLSX Layout 3 ──────────────────────────────────────────────────────────────
# Style: Warm grey/cream tones, invoice details in a top horizontal banner,
#        two-column layout (vendor left / bill-to right), items table with
#        alternating row colour, totals with boxed highlight.
def xlsx_layout_3(inv):
    num, vendor, date, po, amount, *_, lbl, __ = inv
    wb=Workbook(); ws=wb.active; ws.title="Tax Invoice"
    for col,w in zip("ABCDE",[4,30,22,22,24]):
        ws.column_dimensions[col].width=w
    for r,h in {1:6,2:24,3:14,4:14,5:14,6:8,7:14,8:14,9:8,
                10:18,11:18,12:8,13:18,14:18,15:14,16:8,17:18,18:14,19:14}.items():
        ws.row_dimensions[r].height=h

    # Top banner
    ws.merge_cells("B2:E2")
    xc(ws,"B2","TAX INVOICE",bold=True,size=16,bg="4A4A4A",fc="FFFFFF",ha="center")
    ws.merge_cells("B3:E3")
    xc(ws,"B3",f"Invoice No: {num}   |   Date: {date}   |   PO: {po}   |   Terms: Net 30",
       size=9,bg="6D6D6D",fc="EEEEEE",ha="center")

    # Vendor (left) and Bill To (right)
    ws.merge_cells("B5:C5"); xc(ws,"B5","FROM",bold=True,size=8,bg="F0EDEA",fc="555555")
    ws.merge_cells("D5:E5"); xc(ws,"D5","TO",bold=True,size=8,bg="F0EDEA",fc="555555")
    ws.merge_cells("B7:C7"); xc(ws,"B7",vendor,bold=True,size=10,bg="FAF8F5")
    ws.merge_cells("D7:E7"); xc(ws,"D7",BUYER,bold=True,size=10,bg="FAF8F5")
    ws.merge_cells("B8:C8"); xc(ws,"B8",VENDOR_ADDRESS[vendor],size=8,bg="FAF8F5",fc="666666",wrap=True)
    ws.merge_cells("D8:E8"); xc(ws,"D8",BUYER_ADDR,size=8,bg="FAF8F5",fc="666666",wrap=True)
    ws.merge_cells("B9:C9"); xc(ws,"B9",f"GSTIN: {VENDOR_GSTIN[vendor]}",size=8,bg="FAF8F5")
    ws.merge_cells("D9:E9"); xc(ws,"D9",f"GSTIN: {BUYER_GSTIN}",size=8,bg="FAF8F5")

    # Items
    for ci,(h,col) in enumerate(zip(["#","Description of Work / Service","SAC",lbl],"BCDE")):
        xc(ws,f"{col}11",h,bold=True,size=9,bg="4A4A4A",fc="FFFFFF",ha="center",bdr=True)
    for ci,(v,col) in enumerate(zip(["1",VENDOR_DESC[vendor],"998314",f"{amount:,.0f}"],"BCDE")):
        xc(ws,f"{col}12",v,size=9,bg="F7F5F2",ha="center",bdr=True)

    tax=round(amount*0.18); total=amount+tax
    ws.merge_cells("B14:C14"); xc(ws,"B14","Subtotal",size=9,bg="F0EDEA",bdr=True)
    ws.merge_cells("D14:E14"); xc(ws,"D14",f"INR {amount:,.0f}",size=9,ha="right",bg="F0EDEA",bdr=True)
    ws.merge_cells("B15:C15"); xc(ws,"B15","IGST @ 18%",size=9,bdr=True)
    ws.merge_cells("D15:E15"); xc(ws,"D15",f"INR {tax:,.0f}",size=9,ha="right",bdr=True)
    ws.merge_cells("B16:C16"); xc(ws,"B16",lbl,bold=True,size=11,bg="4A4A4A",fc="FFFFFF",bdr=True)
    ws.merge_cells("D16:E16"); xc(ws,"D16",f"INR {total:,.0f}",bold=True,size=11,bg="4A4A4A",fc="FFFFFF",ha="right",bdr=True)

    ws.merge_cells("B18:E18")
    xc(ws,"B18",f"Bank: HDFC Bank  |  A/C: 50200012345678  |  IFSC: HDFC0001234  |  PO: {po}",
       size=7.5,italic=True,fc="999999",ha="center")
    return wb

def draw_xlsx(inv):
    layout=inv[8]
    fn={1:xlsx_layout_1,2:xlsx_layout_2,3:xlsx_layout_3}[layout]
    wb=fn(inv)
    path=f"invoices/input/{inv[0]}.xlsx"
    wb.save(path)
    print(f"  ✓ XLSX (layout {layout}): {path}")

for inv in INVOICES:
    if inv[5]=="XLSX":
        draw_xlsx(inv)

# ─── INVOICE CSV ──────────────────────────────────────────────────────────────
with open("data/invoices.csv","w",newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["invoice_number","vendor_name","invoice_date",
                     "po_number","amount","file_format","expected_result","layout"])
    for inv in INVOICES:
        writer.writerow([inv[0],inv[1],inv[2],inv[3],inv[4],inv[5],inv[6],inv[8]])
print("✓ Created: data/invoices.csv")

# ─── SUMMARY ──────────────────────────────────────────────────────────────────
pdf_count  = sum(1 for i in INVOICES if i[5]=="PDF")
docx_count = sum(1 for i in INVOICES if i[5]=="DOCX")
xlsx_count = sum(1 for i in INVOICES if i[5]=="XLSX")

print("\n"+"="*60)
print("  MOCK DATA GENERATION — COMPLETE")
print("="*60)
print(f"  data/po_master.csv      → {len(PO_MASTER):>2} PO records")
print(f"  data/invoices.csv       → {len(INVOICES):>2} invoice records")
print(f"  PDF invoices            → {pdf_count:>2} files  (3 different layouts)")
print(f"  DOCX invoices           → {docx_count:>2} files  (3 different layouts)")
print(f"  XLSX invoices           → {xlsx_count:>2} files  (3 different layouts)")
print(f"  Total files created     → {2+pdf_count+docx_count+xlsx_count:>2}")
print("="*60)
print("  Test scenario breakdown:")
print(f"    MATCH           : {sum(1 for i in INVOICES if i[6]=='MATCH')}")
print(f"    AMOUNT_MISMATCH : {sum(1 for i in INVOICES if i[6]=='AMOUNT_MISMATCH')}")
print(f"    PO_NOT_FOUND    : {sum(1 for i in INVOICES if i[6]=='PO_NOT_FOUND')}")
print(f"    VENDOR_MISMATCH : {sum(1 for i in INVOICES if i[6]=='VENDOR_MISMATCH')}")
print("="*60)
print("  Layout assignment:")
for inv in INVOICES:
    print(f"    {inv[0]}  {inv[5]:4s}  layout-{inv[8]}  [{inv[6]}]")
print("="*60)
