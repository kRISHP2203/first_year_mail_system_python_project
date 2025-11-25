import unittest

from Mail import Mail
from Personal import Personal
from Confidential import Confidential
from MailboxAgent import MailboxAgent
from Interpreter import gen_emails

def test_mail_class():
    print("Testing Mail class")
    mail = Mail("100", "frm@gre.ac.uk", "to@gre.ac.uk", "1/1/2025", "subject", "tag", "Body sample text")
    mail.show_email()

def test_personal_class():
    print("\nTesting Personal class")
    personal_mail = Personal("101", "email123@gre.ac.uk", "to@gre.ac.uk", "2/2/2025", "subject", "prsnl", "Body example text")
    personal_mail.show_email()

def test_confidential_class():
    print("\nTesting Confidential class")
    conf_mail = Confidential("102", "confidential@gre.ac.uk", "to@gre.ac.uk", "3/3/2025", "subject", "conf", "Body secret message")
    conf_mail.show_email()

def test_mailbox_agent():
    print("\nTesting MailboxAgent")
    # Use gen_emails to generate dummy emails
    dummy_emails = gen_emails()  # returns list of raw email strings
    mba = MailboxAgent(dummy_emails)

    # Test get_email (FA.1)
    print("\nTest get_email with existing id '0':")
    email = mba.get_email("0")
    if email:
        email.show_email()
    else:
        print("Email not found")

    # Test del_email (FA.3)
    print("\nTest del_email with id '0':")
    mba.del_email("0")

    # Test filter (FA.4)
    print("\nTest filter for sender 'email4@gre.ac.uk':")
    mba.filter("email4@gre.ac.uk")

    # Test sort_date (FA.5)
    print("\nTest sort_date:")
    mba.sort_date()

    # Test show_emails (FB.1)
    print("\nTest show_emails:")
    mba.show_emails()

    # Test mv_email (FB.2)
    print("\nTest mv_email moving '1' to 'archive':")
    mba.mv_email("1", "archive")

    # Test mark (FB.3)
    print("\nTest mark email id '2' as read:")
    mba.mark("2", "read")
    print("Test mark email id '2' as flagged:")
    mba.mark("2", "flagged")

    # Test find (FB.4)
    print("\nTest find emails on date '12/0/2025':")
    mba.find("12/0/2025")

    # Test sort_from (FB.5)
    print("\nTest sort_from (sort by sender):")
    mba.sort_from()

    # Test add_email (FA&B.6)
    print("\nTest add_email adding new personal email:")
    mba.add_email("newfrm@gre.ac.uk", "newto@gre.ac.uk", "25/12/2025", "New Year", "prsnl", "Body Happy New Year!")
    mba.show_emails()

def test_interpreter_add_command():
    print("\nTesting Interpreter add command simulation")
    # This is a simplified simulation since interpreter is interactive
    # Instead, directly test add_email in mailbox agent as above
    # Or extend this section with your own interaction simulation if needed

if __name__ == "__main__":
    test_mail_class()
    test_personal_class()
    test_confidential_class()
    test_mailbox_agent()
    test_interpreter_add_command()




if __name__ == '__main__':
    unittest.main()