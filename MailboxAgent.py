#################################################################################################
### COMP1811 - CW1 Outlook Simulator                                                          ###
###            MailboxAgent Class                                                             ###
###            <describe the purpose and overall functionality of the class defined here>     ###
### Partner A:                                                                                ###
###            Parthilkumar Miteshbhai Patel, 001485972                                       ###
### Partner B:                                                                                ###
###            Krish Thakorbhai Patel, 0001495242                                             ###
#################################################################################################


# DO NOT CHANGE CLASS OR METHOD NAMES
# replace "pass" with your own code as specified in the CW spec.

from Mail import Mail
from Confidential import Confidential
from Personal import Personal

class MailboxAgent:
    """<This is the documentation for MailboxAgent. Complete the docstring for this class."""
    def __init__(self, email_data):                       # DO NOT CHANGE
        self._mailbox = self.__gen_mailbox(email_data)    # data structure containing Mail objects DO NOT CHANGE

    # Given email_data (string containing each email on a separate line),
    # __gen_mailbox returns mailbox as a list containing received emails as Mail objects
    @classmethod
    def __gen_mailbox(cls, email_data):                   # DO NOT CHANGE
        """ generates mailbox data structure
            :ivar: String
            :rtype: list  """
        mailbox = []
        for e in email_data:
            msg = e.split('\n')
            mailbox.append(
                Mail(msg[0].split(":")[1], msg[1].split(":")[1], msg[2].split(":")[1], msg[3].split(":")[1],
                     msg[4].split(":")[1], msg[5].split(":")[1], msg[6].split(":")[1]))
        return mailbox

# FEATURES A (Partner A)
    # FA.1
    #
    def get_email(self, m_id):
        """ """
        for mail in self._mailbox:
            if mail.m_id == m_id:
                return mail
        print(f"Error: Email with m_id {m_id} not found")
        return None #if no email found

    # FA.3
    #
    def del_email(self, m_id):
        """  """
        mail = self.get_email(m_id)
        if mail:
            mail.tag = 'bin'
            print(f"Email {m_id} moved to bin.")
            mail.show_email()

    # FA.4
    #
    def filter(self, frm):
        """  """
        found_email = [mail for mail in self._mailbox if frm in mail.frm]

        print(f"Found {len(found_email)} emails with {frm}") #dis
        print(f"{'ID':<5} | {'From':<20} | {'To':<20} | {'Date':<10} | {'Tag':<10}")
        print("-" * 90)

        #print row
        for mail in found_email:
            print(f"{mail.m_id:<5} | {mail.frm:<20} | {mail.to:<20} | {mail.date:<10} | {mail.tag:<10}")

    # FA.5
    #
    def sort_date(self):
        """  """
        self._mailbox.sort(key=lambda mail: mail.date)
        print("Mailbox sorted by date {_date}.}")


# FEATURES B (Partner B)
    # FB.1
    #
    def show_emails(self):
        """  details of personal email """
        for mail in self._mailbox:
            mail.show_email()

    # FB.2
    #
    def mv_email(self, m_id, tag):
        """  """
        mail = self.get_email(m_id)
        if mail:
            mail.tag = tag
            print(f"Email {m_id} moved to folder '{tag}'.")
            mail.show_email()
        else:
            print(f"Email {m_id} not moved to folder '{tag}'.")
    # FB.3
    #
    def mark(self, m_id, m_type):
        """  """
        mail = self.get_email(m_id)

        if m_type == 'read':
            mail.read = True
            print(f"Email {m_id} marked as read.")
        elif m_type == 'flagged':
            mail.flagged = True
            print(f"Email {m_id} marked as flagged.")
        else:
            print("invalid mark type.")
            return

    # FB.4
    #
    def find(self, date):
        """  """
        found_emails = []

        for mail in self._mailbox:
            if mail.date == date:
                found_emails.append(mail)
        print(f"Found {len(found_emails)} emails with '{date}':")

        if len(found_emails) > 0:
            print(f"{'ID':<5} | {'From':<20} | {'To':<20} | {'Date':<10} | {'Suject' :<15} | {'Tag':<10}")
            print("-" * 90)

            for mail in found_emails:
                print(f"{mail.m_id:<5} | {mail.frm:<20} | {mail.to:<20} | {mail.tag:<10} | {mail.date:<10} | {mail.subject:<15} | {mail.tag:<10}")

            else:
                print(f"No emails with date {date} found.")
    # FB.5
    #
    def sort_from(self):
        """  """
        self._mailbox.sort(key=lambda mail: mail.frm)
        print("Mailbox sorted.")

# FEATURE 6 (Partners A and B)
    #
    def add_email(self, frm, to, date, subject, tag, body, m_id=None):
        """  """
        # code must generate unique m_id
        next_id = len(self._mailbox) + 1 #make unique id

        match tag.lower():
            # FA.6
            case 'conf':     # executed when tag is 'conf'
                new_mail = Confidential(next_id, frm, to, date, subject, tag, body)
                self._mailbox.append(new_mail)


                print(f"Confidential added to email with ID {next_id}.")
            # FB.6
            case 'prsnl':    # executed when tag is 'prsnl'
                new_mail = Personal(next_id, frm, to, date, subject, tag, body)
                self._mailbox.append(new_mail)
                print(f"Personal email added with id {m_id}.")
            # FA&B.6
            case _:          # executed when tag is neither 'conf' nor 'prsnl'
                new_mail = Mail(next_id, frm, to, date, subject, tag, body)
                self._mailbox.append(new_mail)
                print(f"General email with id {m_id}.")
