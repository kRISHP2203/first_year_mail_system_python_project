import unittest
from io import StringIO
import sys
from Mail import Mail
from Personal import Personal
from Confidential import Confidential
from MailboxAgent import MailboxAgent
from Interpreter import gen_emails
import datetime

class TestOutlookSimulator(unittest.TestCase):
    def setUp(self):
        """
        Each test starts with a fresh MailboxAgent instance initialized with generated emails
        """
        self.mba = MailboxAgent(gen_emails())

    # ----------------- UNIT TESTING -----------------
    # Test individual functions in isolation

    def test_get_email_found(self):
        """Test that get_email returns an email object for existing m_id"""
        mail = self.mba.get_email("0")
        self.assertIsNotNone(mail)
        self.assertEqual(mail.m_id, "0")

    def test_get_email_not_found(self):
        """Test get_email returns None if m_id not found"""
        mail = self.mba.get_email("9999")
        self.assertIsNone(mail)

    def test_del_email_changes_tag(self):
        """Test that del_email moves an email to the bin and sets deletion date"""
        self.mba.del_email("0")
        mail = self.mba.get_email("0")
        self.assertEqual(mail.tag, "bin")
        self.assertIsInstance(mail._deletion_date, datetime.datetime)

    def test_mark_read_and_flagged(self):
        """Test marking an email as read and flagged updates attributes"""
        self.mba.mark("1", "read")
        mail = self.mba.get_email("1")
        self.assertTrue(mail.read)

        self.mba.mark("1", "flagged")
        # adjust attribute name if needed
        self.assertTrue(hasattr(mail, 'flag') and mail.flag or hasattr(mail, 'flagged') and mail.flagged)

    # ----------------- INTEGRATION TESTING -----------------
    # Test interaction between multiple methods and components

    def test_add_then_get_email(self):
        """Test adding new emails and then retrieving them by m_id"""
        initial_count = len(self.mba._mailbox)

        self.mba.add_email("alice@gre.ac.uk", "bob@gre.ac.uk", "25/12/2025", "Xmas Greetings", "prsnl", "Happy holidays!")
        self.mba.add_email("charlie@gre.ac.uk", "dave@gre.ac.uk", "26/12/2025", "Secret", "conf", "Top secret info.")

        self.assertEqual(len(self.mba._mailbox), initial_count + 2)

        # Check if last added email subject matches
        last_mail = self.mba._mailbox[-1]
        self.assertEqual(last_mail.subject, "Secret")

    def test_del_then_show_emails_output(self):
        """Test deleting (moving to bin) an email and showing mailbox output contains it"""
        self.mba.del_email("0")

        captured_output = StringIO()
        sys.stdout = captured_output

        self.mba.show_emails()

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("bin", output)
        self.assertIn("m_id     :0", output)

    # ----------------- BLACK-BOX TESTING -----------------
    # Test from user perspective by capturing output of commands

    def test_filter_command_output(self):
        """Test filter shows emails from given sender in output"""
        captured_output = StringIO()
        sys.stdout = captured_output

        self.mba.filter("email4@gre.ac.uk")

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("Found", output)
        self.assertIn("email4@gre.ac.uk", output)

    def test_find_command_valid_date(self):
        """Test find command outputs emails matching a valid date"""

        # Get a real date from mailbox for testing
        valid_date = self.mba._mailbox[0].date

        captured_output = StringIO()
        sys.stdout = captured_output

        self.mba.find(valid_date)

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("Found", output)
        self.assertIn(valid_date, output)

    def test_find_command_invalid_date(self):
        """Test find handles invalid date input gracefully"""
        captured_output = StringIO()
        sys.stdout = captured_output

        self.mba.find("invalid-date")

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        self.assertIn("Invalid date format", output)

    # ----------------- TESTS FOR MAIL, PERSONAL, CONFIDENTIAL -----------------

    def test_mail_object_attributes(self):
        """Test Mail object initialization"""
        mail = Mail("100", "frm@gre.ac.uk", "to@gre.ac.uk", "1/1/2025", "subject", "tag", "Body sample")
        self.assertEqual(mail.m_id, "100")
        self.assertEqual(mail.frm, "frm@gre.ac.uk")

    def test_personal_class_body_replacement(self):
        """Test Personal emails replace 'Body' with sender ID in body text"""
        personal_mail = Personal("101", "email142@gre.ac.uk", "to@gre.ac.uk", "5/5/2025", "subject", "prsnl", "This is Body text")
        self.assertIn("email142", personal_mail._body)

    def test_confidential_encryption_differs_body(self):
        """Test Confidential emails encrypt the body"""
        body = "Secret Message"
        conf_mail = Confidential("102", "confidential@gre.ac.uk", "to@gre.ac.uk", "6/6/2025", "subject", "conf", body)
        self.assertNotEqual(conf_mail._body, body)

if __name__ == '__main__':
    unittest.main()
