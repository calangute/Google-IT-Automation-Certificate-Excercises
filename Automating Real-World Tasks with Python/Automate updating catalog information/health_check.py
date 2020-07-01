#!/usr/bin/env python3

import shutil
import psutil
import socket
import emails

subject_reference = {"cpu_usage_error": "Error - CPU usage is over 80%", "disk_space_error": "Error - Available disk space is less than 20%",
                     "memory_limit_error": "Error - Available memory is less than 500MB", "hostname_error": "Error - localhost cannot be resolved to 127.0.0.1"}


def disk_space_alarm():
    du = shutil.disk_usage("/")
    used_percent = round((du.free/du.total)*100, 2)
    if used_percent < 20.00:
        return True


def cpu_usage_alarm():
    if psutil.cpu_percent() > 80:
        return subject_reference["cpu_usage_error"]


def memory_limit_alarm():
    if psutil.virtual_memory() < 524288000:
        return subject_reference["memory_limit_error"]


def localhost_resolution_alarm():
    ip = socket.getaddrinfo("localhost", 0)[-1][-1][0]
    if ip != '127.0.0.1':
        return subject_reference["hostname_error"]


def generate_and_send_email(subject):
    """ constructs and sends email """
    sender = "automation@example.com"
    to = "username@example.com"
    body = "Please check your system and resolve the issue as soon as possible."
    msg = emails.generate_email(sender, to, subject, body)
    emails.send_email(msg)


def alert_for_errors():
    """  controller method  """
    if disk_space_alarm():
        generate_and_send_email(subject_reference["disk_space_error"])
    if cpu_usage_alarm():
        generate_and_send_email(subject_reference["cpu_usage_error"])
    if memory_limit_alarm():
        generate_and_send_email(subject_reference["memory_limit_error"])
    if localhost_resolution_alarm():
        generate_and_send_email(subject_reference["hostname_error"])


if __name__ == '__main__':
    alert_for_errors()