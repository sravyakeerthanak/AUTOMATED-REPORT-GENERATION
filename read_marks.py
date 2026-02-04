from fpdf import FPDF

# Read file
file = open("marks.txt", "r")
lines = file.readlines()
file.close()

marks = []
for line in lines:
    marks.append(int(line.strip()))

total = sum(marks)
average = total / len(marks)

# Create PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.cell(0, 10, "Student Marks Report", ln=True)
pdf.ln(5)

pdf.cell(0, 10, f"Marks: {marks}", ln=True)
pdf.cell(0, 10, f"Total: {total}", ln=True)
pdf.cell(0, 10, f"Average: {average}", ln=True)

pdf.output("report.pdf")

print("PDF created")
