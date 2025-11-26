#################################################################################################
### COMP1811 - CW1 Outlook Simulator                                                          ###
###            Confidential Class                                                             ###
###            The confidential class, inherits from the Mail class. As Confidential emails   ###
###            automatically encrypt and decrypt the email body using ROT13.                  ###
### Partner A:                                                                                ###
###            Parthilkumar Miteshbhai Patel, 001485972                                       ###
#################################################################################################

# DO NOT CHANGE CLASS OR METHOD NAMES
# replace "pass" with your own code as specified in the CW spec.

from Mail import Mail

# FA.5.a
class Confidential(Mail):
    """
    [OOP CONCEPT: Inheritance] Inherits from the Mail class.
    Confidential represents secure emails with an encrypted body.
    The body is encrypted using ROT13 in the constructor and decrypted on demand.

    """
    # DO NOT CHANGE CLASS NAME OR METHOD NAMES/SIGNATURES
    # Add new method(s) as required in CW spec

    def __init__(self, m_id,frm,to,date,subject,tag,body):    # DO NOT MODIFY Attributes
            super().__init__(m_id,frm,to,date,subject,tag,body)   # Inherits attributes from parent class DO NOT MODIFY
            self.encrypt()

    # FA.5.b
    """
    Encrypts the internal body using ROT13.
    Returns: None
    [Learning Source]: Logic for mutation learnt via AI explanation.
         
    """

    # [OOP CONCEPT: Encapsulation]

    def encrypt(self):
        def rot13(text):
            return text.translate(
                    str.maketrans(
                        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
                        "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"))

        self._body = rot13(self._body)



    def decrypt(self):
        def rot13(text):
            return text.translate(
                str.maketrans(
                    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
                    "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"))

        return self.rot13(self._body)

    # FA.5.c
    """
    [OOP CONCEPT: Polymorphism] Overrides Mail.show_email to clarify encryption.
    Prints out all email details, including encrypted body.
    Returns: None
    [Learning Source]: Print formatting based on coursework examples.
        
    """
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

# Class name is CamelCase, method and variable names are snake_case, private variables with underscore