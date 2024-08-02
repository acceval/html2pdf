from jinja2 import Environment, FileSystemLoader
from xhtml2pdf import pisa

# Define a function to convert HTML to PDF
def convert_html_to_pdf(source_html, output_filename):
    with open(output_filename, "w+b") as result_file:
        pisa_status = pisa.CreatePDF(source_html, dest=result_file)
        return pisa_status.err

# Prepare the template environment
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

# Data to fill the template
data = [
    {'name': 'Alice', 'email': 'alice@example.com', 'age': 30},
    {'name': 'Bob', 'email': 'bob@example.com', 'age': 25},
    {'name': 'Carol', 'email': 'carol@example.com', 'age': 27}
]

# Additional variables for the template
context = {
    'title': 'Comprehensive User Information',
    'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/KPMG_logo.svg/2560px-KPMG_logo.svg.png',
    'description': 'This document provides a dynamic overview of user data.',
    'data': data,
    'footer_note': 'This is a generated document. For internal use only.'
}

# Render the HTML
rendered_html = template.render(context)

# Convert to PDF
convert_html_to_pdf(rendered_html, "output.pdf")

print("PDF file has been created successfully!")
