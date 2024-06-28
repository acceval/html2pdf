import pdfkit
from jinja2 import Environment, FileSystemLoader

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
pdfkit.from_string(rendered_html, 'output.pdf')

print("PDF file has been created successfully!")
