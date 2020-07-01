#!/usr/bin/env python3

import reports
import emails
import run
from datetime import date


def process_report_content():
    raw_content = run.get_fruits_data(upload=False)
    content = ""
    # constructing body
    for each in raw_content:
        for k, v in each.items():
            content += "{}".format(k + " :  " + v + "<br/>")
        content += "<br/>"
    return content


if __name__ == '__main__':
    # setting file name
    file_name = "/tmp/processed.pdf"
    # setting title
    today = date.today().strftime("%B %d, %Y")
    title = "Processed Update on {}".format(today)
    # generating report
    reports.generate_report(file_name, title, process_report_content())
    # setting email content
    sender = "automation@example.com"
    to = "username@example.com"
    subject_line = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    # generating and sending email
    msg = emails.generate_email(sender, to, subject_line, body, file_name)
    emails.send_email(msg)



