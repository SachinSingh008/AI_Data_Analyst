# report_generator.py
from jinja2 import Environment, FileSystemLoader
import pdfkit

def generate_report(context, output_path='outputs/report.html'):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('report_template.html')
    html_out = template.render(context)
    with open(output_path, 'w') as f:
        f.write(html_out)
    # Optional: Convert to PDF
    # pdfkit.from_file(output_path, output_path.replace('.html', '.pdf'))
