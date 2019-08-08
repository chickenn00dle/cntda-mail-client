#!/usr/bin/env python3

import argparse
import getpass
import smtplib
import ssl
from email.mime.text import MIMEText

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('my_address', type=str)
    parser.add_argument('mail_server', type=str)
    args = parser.parse_args()
    send_mail(args.my_address, args.mail_server)
    return 0


def send_mail(my_address, mail_server):
    # Start by prompting user for password, recipient, subject, and message text
    password = getpass.getpass(prompt = 'Password for ' + my_address + '\n')
    print('Recipients email address:')
    their_address = input()
    print('Subject line:')
    subject = input()
    print('Message content:')
    message = input()

    # Create msg object
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = my_address
    msg['To'] = their_address

    port = get_port()
    with smtplib.SMTP(mail_server, port) as server:
        try:
            print('Sending...\n')
            context = ssl.create_default_context()
            server.starttls(context=context)
            server.ehlo()
            server.login(my_address, password)
            server.send_message(msg)
        except Exception as err:
            print(err)
    return 0


"""
Return relevant port number. For now only return 587, but we may want to make this more flexible.
"""
def get_port():
    return 587


if __name__ == "__main__":
    main()
