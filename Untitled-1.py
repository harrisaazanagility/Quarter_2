from fpdf import FPDF

# Final cleanup: replace all non-ASCII dashes and special characters with ASCII-compatible versions
def clean_text(text):
    return text.replace("–", "-").replace("—", "-").replace("•", "-").replace("’", "'")

# Example data for selling_points, table_data, and reasons_ascii
selling_points = [
    ("Fuel Efficiency", "The HR-V e:HEV offers excellent fuel economy with its hybrid technology."),
    ("Advanced Safety", "Equipped with Honda Sensing for enhanced driver safety."),
    ("Spacious Interior", "Enjoy a roomy and comfortable cabin for all passengers.")
]

table_data = [
    ["Feature", "HR-V e:HEV", "Other Hybrid SUVs"],
    ["Fuel Economy", "26 km/l", "22 km/l"],
    ["Safety", "Honda Sensing", "Standard"],
    ["Interior Space", "Spacious", "Average"]
]

reasons_ascii = [
    "Best-in-class fuel efficiency and reliability.",
    "Advanced safety features for peace of mind.",
    "Modern design and comfortable ride."
]

# Clean all table data, selling points, and reasons
selling_points_cleaned = [(clean_text(title), clean_text(desc)) for title, desc in selling_points]
cleaned_table_data = [[clean_text(item) for item in row] for row in table_data]
reasons_ascii_cleaned = [clean_text(reason) for reason in reasons_ascii]
# Reinitialize PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Selling Points Section
pdf.set_fill_color(240, 240, 240)
pdf.set_font("Arial", "B", 12)
pdf.set_text_color(0)
pdf.cell(0, 10, "Top Selling Points of Honda HR-V e:HEV", ln=True, fill=True)
pdf.ln(2)

for title, desc in selling_points_cleaned:
    pdf.set_font("Arial", "B", 11)
    pdf.set_text_color(0, 102, 204)
    pdf.cell(0, 10, f"- {title}", ln=True)
    pdf.set_font("Arial", "", 10)
    pdf.set_text_color(0)
    pdf.multi_cell(0, 6, desc)
    pdf.ln(1)

# Comparison Table Section
pdf.add_page()
pdf.set_font("Arial", "B", 12)
pdf.set_fill_color(240, 240, 240)
pdf.cell(0, 10, "HR-V e:HEV vs Other Hybrid SUVs", ln=True, fill=True)
pdf.ln(4)

pdf.set_font("Arial", "B", 10)
# Define column widths based on page width and number of columns
num_cols = len(cleaned_table_data[0])
page_width = pdf.w - 2 * pdf.l_margin
col_widths = [page_width / num_cols] * num_cols

for row_idx, row in enumerate(cleaned_table_data):
    for col_idx, item in enumerate(row):
        fill = row_idx == 0
        pdf.set_fill_color(200, 220, 255) if fill else pdf.set_fill_color(255)
        pdf.cell(col_widths[col_idx], 8, item, border=1, align="C", fill=fill)
    pdf.ln()

# Why Choose Section
pdf.add_page()
pdf.set_font("Arial", "B", 12)
pdf.set_text_color(0)
pdf.set_fill_color(240, 240, 240)
pdf.cell(0, 10, "Why Choose Honda HR-V e:HEV?", ln=True, fill=True)
pdf.ln(3)

for reason in reasons_ascii_cleaned:
    pdf.cell(0, 8, reason, ln=True)

# Contact Info Section
pdf.ln(10)
pdf.set_font("Arial", "B", 11)
pdf.set_text_color(220, 0, 0)
pdf.cell(0, 10, "For Test Drive & Booking:", ln=True)
pdf.set_font("Arial", "", 11)
pdf.set_text_color(0)
pdf.cell(0, 8, "Honda Sahiwal", ln=True)
pdf.cell(0, 8, "Sahiwal Bypass, Sahiwal, 57000", ln=True)
pdf.cell(0, 8, "Tel: 0333-1225555 / 0309-8888979", ln=True)

# Save the final cleaned PDF
final_pdf_path = "/mnt/data/Honda_HRV_eHEV_Brochure.pdf"
pdf.output(final_pdf_path)

final_pdf_path
