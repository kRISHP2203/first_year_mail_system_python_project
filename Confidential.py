#################################################################################################
### COMP1811 - CW1 Outlook Simulator                                                          ###
###            Confidential Class                                                             ###
###            <describe the purpose and overall functionality of the class defined here>     ###
### Partner A:                                                                                ###
###            Parthilkumar Miteshbhai Patel, 001485972                                       ###
#################################################################################################

# DO NOT CHANGE CLASS OR METHOD NAMES
# replace "pass" with your own code as specified in the CW spec.

from Mail import Mail

# FA.5.a
class Confidential(Mail):
    """ """
    # DO NOT CHANGE CLASS NAME OR METHOD NAMES/SIGNATURES
    # Add new method(s) as required in CW spec

    def __init__(self, m_id,frm,to,date,subject,tag,body):    # DO NOT MODIFY Attributes
            super().__init__(m_id,frm,to,date,subject,tag,body)   # Inherits attributes from parent class DO NOT MODIFY
            self.encrypt()

    # FA.5.b
    #


    def encrypt(self):

        def rot13(text):
            return text.translate(
                    str.maketrans(
                        "ABCDEFGHIJKLMNOPQRSTUVWXYZ12345abcdefghijklmnopqrstuvwxyz",
                        "NOPQRSTUVWXYZABCDEFGHIJKLM09876nopqrstuvwxyzabcdefghijklm"))

        self._body = rot13(self._body)

    def decrypt(self):
        def rot13(text):
            return text.translate(
                    str.maketrans(
                        "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234abcdefghijklmnopqrstuvwxyz",
                        "NOPQRSTUVWXYZABCDEFGHIJKLM09876nopqrstuvwxyzabcdefghijklm"))
        return rot13(self._body)


    # FA.5.c
    def show_email(self):
            """Overrides the base class show_email method to indicate the content is encrypted. """

            print("-" * 40)
            print(f"CONFIDENTIAL EMAIL (Encrypted)")
            print(f"m_id      : {self.m_id}")
            print(f"frm       : {self.frm}")
            print(f"to       :{self.to}")
            print(f"date     :{self.date}")
            print(f"subject  :{self.subject}")
            print(f"tag      :{self.tag}")
            print(f"read     :{'Yes' if self.read else 'No'}")
            print(f"flag     :{'Yes' if self.flag else 'No'}")
            print("body:")
            print(self._body)
            print("-" * 40)
