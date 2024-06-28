### Dynamic PDF Generator

This project provides a Python script that dynamically generates a PDF document using HTML templates filled with user-defined data. It utilizes Jinja2 for template rendering and pdfkit for converting the rendered HTML to a PDF file. 
Features
- Dynamic Content Rendering: Utilizes Jinja2 to inject data into HTML templates.
- PDF Conversion: Converts the dynamically generated HTML document into a PDF file using pdfkit.
- Customizable Layout: Easy to modify HTML and CSS for custom styling and layout adjustments.
- Comprehensive Template Example: Includes placeholders for a title, description, image, data table, and footer note.

### Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- pdfkit
- wkhtmltopdf
- Jinja2

You can install the necessary Python packages using pip:
```pip install pdfkit Jinja2```

For ```wkhtmltopdf```, follow the installation instructions based on your operating system:

- Ubuntu/Debian: sudo apt-get install wkhtmltopdf
- Windows: Download from wkhtmltopdf.org and add it to your system path.
- macOS: Use Homebrew: brew install wkhtmltopdf
### Usage
1. Prepare Your Data: Modify the data list in the script to include what you wish to list in the PDF.
2. Modify the Template (Optional): Adjust template.html to fit your layout and styling preferences.
3. Run the Script: Execute the script to generate the PDF.
 ```python main.py```
4. This will create a PDF file named output.pdf in your working directory.
5. View the PDF: Open output.pdf with any standard PDF viewer to see the results.

### Customization

To customize the content of the PDF:
- Edit the template.html file to change the HTML structure and CSS.
- Modify the context dictionary in the Python script to adjust the data passed to the HTML template.
