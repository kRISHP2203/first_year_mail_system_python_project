import unittest
from MailboxAgent import MailboxAgent
from Mail import Mail
from Confidential import Confidential
from Personal import Personal

class TestMailboxAgent(unittest.TestCase):

    def setUp(self):
        """Prepare a mailbox agent with sample emails."""
        self.mba = MailboxAgent([])

        self.e1 = Mail("1", "a@gre.ac.uk", "b@gre.ac.uk", "2024/07/26", "Hi", "inbox", "Body one")
        self.e2 = Personal("2", "x@gre.ac.uk", "y@gre.ac.uk", "2025/08/19", "Update", "prsnl", "Body two")
        self.e3 = Mail("3", "z@gre.ac.uk", "a@gre.ac.uk", "2025/06/25", "Meeting", "inbox", "Body three")
        self.e4 = Confidential("4", "bank@secure.com", "me@gre.ac.uk", "2023/03/15","Account", "conf", "Balance 11119")
        self.mba._mailbox = [self.e1, self.e2, self.e3, self.e4]

    def test_get_email_valid(self):
        result = self.mba.get_email("1")
        self.assertEqual(result.m_id, "1")
        self.assertEqual(result.frm, "a@gre.ac.uk")
    def test_get_email_invalid(self):
        self.assertIsNone(self.mba.get_email("1000"))

    def test_delete_email(self):
        self.mba.del_email("2")
        email = self.mba.get_email("2")
        self.assertEqual(email.tag, "bin")

    def test_filter_sender(self):
        # returns from filter not used, so count from mailbox
        self.mba.filter("a@gre.ac.uk")
        matches = [m for m in self.mba._mailbox if "a@gre.ac.uk" in m.frm]
        self.assertEqual(len(matches), 1)

    def test_confidential_is_encrypted(self):
        self.assertNotEqual(self.e4._body, "Balance 11119")
        # Should decrypt to original
        self.assertEqual(self.e4.decrypt(), "Balance 11119")

    def test_add_general_mail(self):
        self.mba.add_email("h@gre.ac.uk", "i@gre.ac.uk", "2025/03/05","New", "tag1", "Test Body")
        last = self.mba._mailbox[-1]
        self.assertIsInstance(last, Mail)
        self.assertEqual(last.frm, "h@gre.ac.uk")

    def test_add_confidential_mail(self):
        self.mba.add_email("p@gre.ac.uk", "q@gre.ac.uk", "2025/03/06","Hidden", "conf", "Some secret")
        last = self.mba._mailbox[-1]
        self.assertIsInstance(last, Confidential)
        self.assertNotEqual(last._body, "Some secret")  # encrypted
        self.assertEqual(last.decrypt(), "Some secret")

    def test_mark_and_flag(self):
        self.mba.mark("1", "read")
        mail = self.mba.get_email("1")
        self.assertTrue(mail.read)
        self.mba.mark("1", "flagged")
        self.assertTrue(mail.flag)

    def test_mark_all_as_read(self):
        self.mba.mark_all_as_read()
        for mail in self.mba._mailbox:
            self.assertTrue(mail.read)

    def test_find_by_date(self):
        # Should find one with 2024/07/26
        self.mba.find("2024/07/26")
        found = [m for m in self.mba._mailbox if m.date == "2024/07/26"]
        self.assertEqual(len(found), 1)

    def test_sort_from(self):
        self.mba.sort_from()
        frm_list = [m.frm for m in self.mba._mailbox]
        self.assertEqual(frm_list, sorted(frm_list))

    def test_sort_date(self):
        self.mba.sort_date()
        date_list = [m.date for m in self.mba._mailbox]
        self.assertEqual(date_list, sorted(date_list))

    def test_move_confidential_to_prsnl(self):
        self.mba.mv_email("4", "prsnl")
        mail = self.mba.get_email("4")
        self.assertIsInstance(mail, Personal)
        self.assertEqual(mail.tag, "prsnl")
        self.assertIn("bank", mail._body)  # Personal puts id in body

    def test_move_prsnl_to_confidential(self):
        self.mba.mv_email("2", "conf")
        mail = self.mba.get_email("2")
        self.assertIsInstance(mail, Confidential)
        self.assertNotEqual(mail._body, "Body two")  # encrypted
        self.assertIn("x", mail.decrypt())  # sender id

    def test_delete_and_cleanup_bin(self):
        self.mba.del_email("3")
        import datetime
        mail = self.mba.get_email("3")
        mail._deletion_date = datetime.datetime.now() - datetime.timedelta(days=11)
        self.mba.cleanup_bin()
        self.assertIsNone(self.mba.get_email("3"))

if __name__ == '__main__':
    unittest.main()
