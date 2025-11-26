#################################################################################################
### COMP1811 - CW1 Outlook Simulator                                                          ###
###            Personal Class                                                                 ###
###            The purpose of this personal email class is, that it inherits from the base    ###
###            Mail class.   ###
###  ###
### Partner B:                                                                                ###
###            Krish Thakorbhai Patel, 0001495242                                             ###
#################################################################################################

# DO NOT CHANGE CLASS OR METHOD NAMES/SIGNATURES
# replace "pass" with your own code as specified in the CW spec.

from Mail import Mail

# FB.5.a
class Personal(Mail):
    """ A personal mail that inherits from mail,
    which automatically replaces the body with the sender uid,
    """
    # DO NOT CHANGE CLASS NAME OR METHOD NAMES/SIGNATURES
    # Add new method(s) as required in CW spec
    def __init__(self, m_id, frm, to, date, subject, tag, body):  # DO NOT MODIFY Attributes
        super().__init__(m_id, frm, to, date, subject, tag, body)  # Inherits attributes from parent class DO NOT MODIFY

        self.add_stats()

    # FB.5.b

    def add_stats(self):
        """
        # 1. Get the sender's UID (e.g. 'email142' from 'email142@gre.ac.uk')
        uid = self._frm.split('@')[0]
        # 2. Replace "Body" in the email text with the UID
        self._body = self._body.replace("Body", uid)
        # 3. Define 'words' by splitting the NEW body text
        words = self._body.split()
        # 4. Calculate stat
        s """

        uid = self._frm.split('@')[0]
        self._body = self._body.replace("Body", uid)

        words = self._body.split()

        if words:
            word_count = len(words)
            total_length = sum(len(word) for word in words)
            avg_length = total_length / word_count #division
            longest_length = len(max(words, key=len))

        else:                        # its handles the case when the body is empty.
            word_count = 0
            avg_length = 0
            longest_length = 0

        # stats formats the information
        stats_text = (
            f"\n\n[Stats] Words: {word_count}"
            f"\n[Stats] Average length: {avg_length}"
            f"\n[Stats] Longest length: {longest_length}"
    )
        self._body += stats_text    #