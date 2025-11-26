#################################################################################################
### COMP1811 - CW1 Outlook Simulator                                                          ###
###            MailboxAgent Class                                                             ###
###            This file defines the mailboxagent class, which acts as the controller for all ###
###            mailbox operation. Adding, removing and sorting emails through appropriate     ###
###            methods. It upholds OOP concept by managing a private mailbox collection       ###
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
import datetime

class MailboxAgent:
    """
    [OOP CONCEPT: Encapsulation]
    Represents a user's mailbox and provides all email operations:
    creation, deletion, marking, sorting, filtering, and more.
    The underlying email list (_mailbox) is only accessed here.

    """
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

    def get_email(self, m_id):
        """
            Fetches and returns an email by its ID.
            Args: m_id (str): The email ID to find.
            Returns:Mail/Personal/Confidential or None if not found.
        """
        m_id = str(m_id)
        for mail in self._mailbox:
            if mail.m_id == m_id:
                return mail
        print(f"Error: Email with m_id {m_id} not found")
        return None #if no email found

    # FA.3
    #
    def del_email(self, m_id):
        """
            Moves the email to the bin by changing its tag and adding a deletion date.
            Args:m_id (str): The email ID to delete.
            [OOP CONCEPT: Encapsulation] - Only agent can change tag.
        """
        mail = self.get_email(m_id)
        if mail:
            mail.tag = 'bin'
            mail._deletion_date = datetime.datetime.today()
            print(f"Email {m_id} moved to bin on {mail._deletion_date.strftime('%y-%m-%d')} and will be deleted permanently after 10 days")
            mail.show_email()

    def cleanup_bin(self):      #oop
        """
            Removes emails from bin if more than 10 days have passed since their deletion date.
            [Learning Source]: Timedelta and datetime learnt from Python docs.
        """
        today = datetime.datetime.today()
        bin_emails = [mail for mail in self._mailbox if mail.tag == 'bin']

        for mail in bin_emails:
            if mail._deletion_date and ( today - mail._deletion_date).days >= 10:
                self._mailbox.remove(mail)
                print(f"Email {mail.m_id} will permanently removed from bin on {mail._deletion_date}. ")

    # FA.4
    #
    def filter(self, frm):
        """
        Finds and prints emails matching a partial/full sender string.
        """
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
        """
        Sorts the mailbox in place by email date.
        """
        def parse_date(d):
            try:
                day, month, year = map(int, d.split('/'))
                return datetime.date(year, month, day)
            except:
                print(f"Invalid date format in mailbox: {d}")
                return datetime.date.max

        self._mailbox.sort(key=lambda mail: mail.date)
        print("Mailbox sorted by date {_date}.}")


# FEATURES B (Partner B)
    # FB.1
    #
    def show_emails(self):
        """
        Prints a formatted table listing of all emails in the mailbox.
        """
        print(f"{'ID':<5} | {'From':<20} | {'To':<20} | {'Date':<10}  | {'Subject':<15} | {'Tag':<10} |  {'Read':<15} | {'Flag':<15}")
        print("-" * 150)
        for mail in self._mailbox:
            read_status = 'Yes' if mail.read else 'No'
            flagged_status = 'Yes' if getattr(mail, 'flag', False) or getattr(mail, 'read', False) else 'No'
            print(f"{mail.m_id:<5} | {mail.frm:<20} | {mail.to:20} | {mail.date:<10} | {mail.subject:<15} |  {mail.tag:<10} | {read_status:<15} | {flagged_status:<15}")

    # FB.2
    #
    def mv_email(self, m_id, tag):
        """
        Changes the tag (folder) of the specified email and updates its type if switching
        to/from confidential. Handles encryption and decryption for conf.
        [OOP CONCEPT: Polymorphism] - Converts and replaces Mail subtype as necessary.
        """
        mail = self.get_email(m_id)
        if not mail:
            print(f"Email {m_id} not found.")
            return

        old_tag = mail.tag

            #move to conf

        if tag == 'conf' and old_tag != 'conf':
            new_mail = Confidential(mail.m_id, mail.frm, mail.to, mail.date, mail.subject, mail.tag, mail.body)

            index = self._mailbox.index(mail)
            self._mailbox[index] = new_mail
            print(f"Email {m_id} moved to confidential files '{tag}'.")
            new_mail.show_email()

        elif old_tag == 'conf' and tag != 'conf':
                #
            decrypted_body = mail.decrypt_bodyz() #
            if tag == 'prsnl':
                new_mail = Personal(mail.m_id, mail.frm, mail.to, mail.date, mail.subject, mail.tag, decrypted_body)
            else:
                new_mail = Mail(mail.m_id, mail.frm, mail.to, mail.date, mail.subject, mail.tag, decrypted_body)
            index = self._mailbox.index(mail)
            self._mailbox[index] = new_mail
            print(f"Email {m_id} moved fromn confidentail files to '{tag}'.")
            new_mail.show_email()
        else:
                mail.tag = tag
                print(f"Email {m_id} moved to folder '{tag}'.")
                mail.show_email()

    # FB.3
    #

    def mark(self, m_id, m_type):
        """
        Mark a particular email as read or flagged.
        [OOP CONCEPT: Encapsulation] - Only agent sets read/flag.
        """
        mail = self.get_email(m_id)

        if m_type == 'read':
            mail.read = True
            print(f"Email {m_id} marked as read.")

        elif m_type == 'flagged':
            mail.flag = True
            print(f"Email {m_id} marked as flagged.")
        else:
            print("invalid mark type.")
            return

    def mark_all_as_read(self):   #oops
        #Marks all emails in the mailbox as read
        for mail in self._mailbox:
            mail.read = True
        print(f"All emails are marked as read.")


    # FB.4
    #
    def find(self, date):
        """
        Finds all emails received on a given date and prints them.
        """

        found_emails = []
        date = date.strip()
        #sdbvjhsb
        for mail in self._mailbox:
            mail_date = mail.date.strip()
            if mail_date == date:
                found_emails.append(mail)

        print(f"Found {len(found_emails)} emails with date '{date}':")
        if found_emails:
            print(f"{'ID':<5} | {'From':<20} | {'To':<20} | {'Date':<10} | {'Subject' :<15} | {'Tag':<10}")
            print("-" * 90)

            for mail in found_emails:
                print(f"{mail.m_id:<5} | {mail.frm:<20} | {mail.to:<20} | {mail.tag:<10} | {mail.date:<10} | {mail.subject:<15} | {mail.tag:<10}")

            else:
                print(f"No emails with date {date} found.")


    # FB.5
    #
    def sort_from(self):
        #Sorts the mailbox in place by email date.
        self._mailbox.sort(key=lambda mail: mail.frm)
        print("Mailbox sorted.")

# FEATURE 6 (Partners A and B)
    #
    def add_email(self, frm, to, date, subject, tag, body, m_id=None):
        """
        Adds a new email to the mailbox, creating the correct email type.
        [OOP CONCEPT: Polymorphism] - Can create different subclasses of Mail.
        [Learning Source]: AI/explained decision logic, W3Schools for match/case.
        """
        # code must generate unique m_id
        next_id = str(len(self._mailbox)) #make unique id

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
            case 'pri':          # executed when tag is neither 'conf' nor 'prsnl'
                new_mail = Mail(next_id, frm, to, date, subject, tag, body)
                self._mailbox.append(new_mail)
                print(f"General email with id {m_id}.")

# Class name and method names follow PEP8. Variable names are snake_case and descriptive.

