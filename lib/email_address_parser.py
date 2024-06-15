# lib/email_address_parser.py

import re

class EmailAddressParser:
    def __init__(self, email_string):
        self.email_string = email_string

    def parse(self):
        # Regular expression to find email addresses
        pattern = r'[\w\.-]+@[\w\.-]+'
        emails = re.findall(pattern, self.email_string)
        return emails

