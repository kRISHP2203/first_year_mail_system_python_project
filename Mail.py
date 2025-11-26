#################################################################################################
### COMP1811 - CW1 Outlook Simulator                                                          ###
###            Mail Class                                                                     ###
###            The mail class file defines, a base class representing an email messaging      ###
###            system similar to outlook                                                      ###
###            Th class provides core data (sender, (sender, receiver, subject, body, flags), ###
###            and provides methods to access and diplay the information.                     ###
### Partner A:                                                                                ###
###            Parthilkumar Miteshbhai Patel, 001485972                                       ###
### Partner B:                                                                                ###
###            Krish Thakorbhai Patel, 0001495242                                             ###
#################################################################################################

# DO NOT CHANGE CLASS OR METHOD NAMES
# replace "pass" with your own code as specified in the CW spec.

class Mail:
    """ """
    # DO NOT CHANGE CLASS OR METHOD NAMES
    def  __init__(self,m_id,frm,to,date,subject,tag,body):    #Create a new Mail object which is an oop concept: Encapsulation
        self._m_id = m_id
        self._frm = frm
        self._to = to
        self._subject = subject
        self._date = date
        self._tag = tag      # reference to Outlook mail folder email is stored in
                             # e.g. tag0 = inbox, tag1 = bin, tag2 = private, tag3 = bank_acct, tag4 = COMP1811, etc.
        self._body = body
        self._flag = False   # Boolean indicating whether email is important
        self._read = False   # Boolean indicating whether the email is read or not.

    # Format should be done from pretty print.
    def __str__(self):
        return f"m_id:{self.m_id}\tfrom:{self.frm}\t|{self.to}\t|{self.date}|{self.subject}|{self.tag}|{self.read}|{self.flag}"

    @property
    def m_id(self):
        return self._m_id

    @property
    def frm(self):
        return self._frm

    @property
    def to(self):
        return self._to

    @property
    def date(self):
        return self._date

    @property
    def body(self):
        return self._body

    @property
    def subject(self):
        return self._subject

    @property
    def tag(self):
        return self._tag

    @property
    def read(self):
        return self._read

    @property
    def flag(self):
        return self._flag

    @tag.setter
    # Pre: value in tags.
    def tag(self, value):
        self._tag = value

    @read.setter
    def read(self,value):
        self._read = value

    @flag.setter
    def flag(self,value):
        self._flag = value

# FEATURES A (Partner A)
    # FA.2
    #show_email prints ull message detail for user display.
    def show_email(self):
        """  print all message detail for user display """
        print(f"m_id     :{self.m_id}")
        print(f"frm      :{self.frm}")
        print(f"to       :{self.to}")
        print(f"date     :{self.date}")
        print(f"subject  :{self.subject}")
        print(f"tag      :{self.tag}")
        print(f"read     :{'Yes' if self.read else 'No'}")
        print(f"flag     :{'Yes' if self.flag else 'No'}")
        print("body:")
        print(self.body)
        print("-" * 40)

