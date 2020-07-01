#!/usr/bin/env python3

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer


def generate_report(file_name_full, title, content):
    style = getSampleStyleSheet()
    report = SimpleDocTemplate(file_name_full)
    empty_line = Spacer(1,20)
    p1 = Paragraph(title, style['h1'])
    p2 = Paragraph(content, style['BodyText'])
    report.build([p1, empty_line, p2, empty_line])
