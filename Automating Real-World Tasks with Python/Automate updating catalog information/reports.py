from reportlab.platypus import SimpleDocTemplate,Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from datetime import date


def generate_report(file_name_full, title, content):
    sample_style_sheet = getSampleStyleSheet()
    mydoc = SimpleDocTemplate(file_name_full)
    p1 = Paragraph(title, sample_style_sheet['Heading1'])
    p2 = Paragraph(content, sample_style_sheet['BodyText'])
    mydoc.build([p1,p2])


if __name__ == '__main__':
    today = date.today().strftime("%B %d, %Y")
    file_name = "hello.pdf"
    ti = "Processed Update on {}".format(today)
    content = "Hakunamattataaaaa <br\> physically fir physically physically physically fit"
    generate_report(file_name,ti,content)
