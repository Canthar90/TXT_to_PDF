from fpdf import FPDF
import glob
from pathlib import Path


filepaths = glob.glob("txt_files/*.txt")
pdf = FPDF(orientation="P", unit="mm", format="A4")
for filepath in filepaths:
    with open(filepath, 'r') as file:
        content = file.read()
    filename = Path(filepath).stem
    
    pdf.add_page()
    pdf.set_font(family="Times", size=18, style="B")
    pdf.cell(w=210, h=8, txt=filename)
    pdf.set_font(family="Times", size=10, style="")
    pdf.write(h=9, txt=content)
pdf.output("Merged.pdf")