

from lib.email_address_parser import EmailAddressParser

def test_parses_emails_with_spaces():
    parser = EmailAddressParser("talk@talk.com john.jones@flatironschool.com alexa@amazon.com")
    assert parser.parse() == ["talk@talk.com", "john.jones@flatironschool.com", "alexa@amazon.com"]

def test_parses_emails_with_commas():
    parser = EmailAddressParser("talk@talk.com,john.jones@flatironschool.com,alexa@amazon.com")
    assert parser.parse() == ["talk@talk.com", "john.jones@flatironschool.com", "alexa@amazon.com"]

def test_parses_emails_with_commas_and_spaces():
    parser = EmailAddressParser("talk@talk.com, john.jones@flatironschool.com, alexa@amazon.com")
    assert parser.parse() == ["talk@talk.com", "john.jones@flatironschool.com", "alexa@amazon.com"]

def test_parses_emails_with_commas_and_spaces_and_non_emails():
    parser = EmailAddressParser("talk@talk.com, what john.jones@flatironschool.com, who alexa@amazon.com, where when why")
    assert parser.parse() == ["talk@talk.com", "john.jones@flatironschool.com", "alexa@amazon.com"]
