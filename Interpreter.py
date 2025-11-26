#################################################################################################
### COMP1811 - CW1 Outlook Simulator                                                          ###
###            Interpreter program                                                            ###
###            Used to as the main program that program will manage all OutlookSim operations ###
###            automatically in response to user commands via an interactive command-line     ###
###            interface. The interpreter represents the user interacting with their mailbox. ###
### Partner A:                                                                                ###
###            Parthilkumar Miteshbhai Patel, 001485972                                       ###
### Partner B:                                                                                ###
###            Krish Thakorbhai Patel, 001495242                                              ###
#################################################################################################

# DO NOT CHANGE FUNCTION NAMES
# replace "pass" with your own code as specified in the CW spec.

from MailboxAgent import *
import random, string

# gen_bdy Generates random text for the email body
# DO NOT MODIFY
def gen_bdy():
    """ generates email body message
        :rtype: string """
    snt = ''
    for i in range(random.randint(1,10)):
        snt += ''.join(random.choices(string.ascii_lowercase, k=random.randint(3,10)))+' '
    return f"Body{str(random.randint(0, 140))}. {snt.capitalize()[:-1]}."

# gen_msg generates a string of emails separated by "----"
#    Used to simulate emails in Outlook mailboxes
#    The output is a string of emails that should be used in your code as required in the CW spec.
# DO NOT MODIFY
def gen_emails():
    """ generates list of email strings
        :rtype: list """
    msgs, msg_id = [], 0
    for i in range(14):     # sent 40 email
        msg = ''
        for j in range(30): # to 30 destinations each
            msg += f"ID:{str(msg_id)}"+"\n"
            msg += f"From:email{random.randint(0, 15)}@gre.ac.uk\n"
            msg += f"To:email{random.randint(0, 80)}@gre.ac.uk\n"
            msg += f"Date:{random.randint(1, 29)}/{random.randint(0, 12)}/2025\n"
            msg += f"Subject:subject{random.randint(0, 100)}\n"
            msg += f"Tag:tag{random.randint(0, 6)}\n"
            msg += f"Body:{gen_bdy()}\n"
            msg += "Flag:False\n"
            msg += "Read:False\n"
        msgs.append(msg)
        msg_id += 1
    return msgs

# DO NOT MODIFY
def display_command_help(): # DO NOT MODIFY (used in loop function)
    """ Displays command line help """
    print('Interpreter Commands:')
    print('get <m_id> | ',      # A.1&2 Command to get and display email given email ID - e.g. get 10
          'lst | ',             # B.1 Display entire mailbox - e.g. lst
          'mv <m_id> <tag> | ', # B.2 Move email with given ID to folder indicated in given tag - e.g. mv 10 conf (i.e. change current tag to conf), then display that email
          'del <m_id> | ',      # A.3 Delete email with given ID by moving to bin - e.g. del 10 (i.e. change current tag to bin), then display that email
          'mrkr <m_id> | ',     # B.3 Mark email with given ID as Read then display that email
          'mrkf <m_id> | ',     # B.3 Mark email with given ID as Flagged then display that email
          'flt <frm> | ',       # A.4 Filter and display all emails from a given name/email address - e.g. flt email13
          'fnd <date> | ',      # B.4 Find and display all emails received on a given date - e.g. fnd 12/3/2025
          'add <email> | '      # A.5&6 and B.5&6 simulate send email by adding emails to the mailbox
          'read all <readall>') # example add prompts:
                                # add email1223@gre.ac.uk email723@gre.ac.uk 29/5/2025 subject99 conf %%Body99911. Isfeo afwco sxzmp.
                                # add email142@gre.ac.uk email788@gre.ac.uk 29/5/2025 subject88 prsnl %%Body11445. Isfffffeo afffwco sxzmp.
                                # add email116@gre.ac.uk email142@gre.ac.uk 29/5/2025 subject36 tag1 %%Body:Body68. Wods vmm tskgdrxzrk.

# loop repeatedly asks for command input until 'end' is entered
# DO NOT MODIFY FUNCTION NAME
# - Replace 'pass' with the code necessary to call class/methods relevant for each command
# - Completed as a group
def loop(before_body=None):
    mba = MailboxAgent(gen_emails())    # mba is an instance of the MailboxAgent class DO NOT MODIFY
    display_command_help()              # simply display the interpreter command-line commands as help
    line = input('mba > ')              # displays a command-line prompter for users to enter command script
    words = line.split(' ')             # separates the command from the script arguments
    command, args = words[0],words[1:]  # command is one of the interpreter script commands outlined in the help above
                                        # args is a list of arguments each command may take.
    while command != 'end':
        match command:
            # Partners A and B
            # Replace each pass statement below with a call to the relevant mba methods as described in the CW spec
            # FA/B.6
            case 'add':
                # example command prompt:
                # add email1223@gre.ac.uk email723@gre.ac.uk 29/5/2025 subject99 conf %%Body99911. Isfeo afwco sxzmp.
                # add email142@gre.ac.uk email788@gre.ac.uk 29/5/2025 subject88 prsnl %%Body11332. Isfffffeo sxzmp.
                # add email116@gre.ac.uk email142@gre.ac.uk 29/5/2025 subject36 tag1 %%Body:Body68. Wods vmm tskgdrxzrk.
                if len(args) < 6:
                    print("Usage: add <frm> <to> <date> <subject> <tag> <body>")
                else:
                    frm, to, date, subject, tag = args[:5]
                    body_args = args[5:]
                    if body_args[0].startswith('%%'):
                        body_args[0] = body_args[0][2:]
                    body = ' '.join(body_args).strip()
                    if not body:
                        print("Error: Empty body")
                    else:
                        mba.add_email(frm, to, date, subject, tag, body)

                        print(f"\n---Mailbox after addtion ---")
                        mba.show_emails()

            case 'del':  # move email with given ID to bin folder
                # example command prompt:
                # del 10
                if len(args) == 1:
                    mba.del_email(args[0])
                else:
                    print("Usage: del <m_id>")

            case 'flt':
                # example command prompt:
                # flt email13
                if len(args) == 1:
                    mba.filter(args[0])
                else:
                    print("Usage: flt <frm>")

            case 'fnd':
                # example command prompt:
                # fnd 12/3/2025
                if len(args) == 1:
                    mba.find(args[0])
                else:
                    print("Usage: fnd <date>")

            case 'get' :                # retrieve and display email Mail object given email ID
                # example command prompt:
                # get 10
                if len(args) == 1:
                    mail = mba.get_email(args[0])
                    if mail:
                        mail.show_email()
                else:
                    print("Usage: get <m_id>")

            case 'lst' :                # display entire mailbox
                # example command prompt:
                # lst
                mba.show_emails()

            case 'mrkr':
                # example command prompt:
                # mrkr 10
                if len(args) == 1:
                    mba.mark(args[0], 'read')
                    mail = mba.get_email(args[0])
                    if mail:
                        mail.show_email()
                else:
                    print("Usage: mrkr <m_id>")

            case 'readall':                  #oops
                mba.mark_all_as_read()

            case 'mrkf':
                # example command prompt:
                # mrkf 10
                if len(args) == 1:
                    mba.mark(args[0], 'flagged')

                else:
                    print("Usage: mrkf <m_id> ")

            case 'mv':                  # move email with given ID to folder in given tag
                # example command prompt:
                # mv 10 conf
                if len(args) == 2:
                    mba.mv_email(args[0], args[1])
                else:
                    print("Usage: mv <m_id> <tag> ")


        line = input('mba > ')
        words = line.split(' ')
        command, args = words[0], words[1:]

if __name__ == '__main__':
    loop()

