from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import datetime

# Create a PDF report
class PDFReport:
    def __init__(self, filename):
        self.filename = filename
        self.pdf = canvas.Canvas(self.filename, pagesize=letter)
        self.width, self.height = letter

    def create_title(self, title):
        self.pdf.setFont('Helvetica-Bold', 16)
        self.pdf.drawString(100, self.height - 50, title)

    def add_section(self, title, content):
        self.pdf.setFont('Helvetica-Bold', 12)
        self.pdf.drawString(100, self.pdf._y, title)
        self.pdf.setFont('Helvetica', 10)
        text = self.pdf.beginText(100, self.pdf._y - 20)
        text.textLines(content)
        self.pdf.drawText(text)
        self.pdf._y -= 50  # space between sections

    def save(self):
        self.pdf.save()

# Generate PDF report
if __name__ == '__main__':
    report = PDFReport('documentation_report.pdf')
    report.create_title('Comprehensive PDF Report')

    report.add_section('P0 Documentation', 'P0 documentation details go here.')
    report.add_section('P1 Documentation', 'P1 documentation details go here.')
    report.add_section('P2 Documentation', 'P2 documentation details go here.')
    report.add_section('P3 Documentation', 'P3 documentation details go here.')
    report.add_section('Code Samples', 'Code sample details go here.')
    report.add_section('Performance Results', 'Performance results details go here.')

    report.save()  
