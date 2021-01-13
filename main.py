from random import *
import smtplib
def main():
    output=''
    l=int(input('Choose approx. password length: '))
    for i in range(l):
      output+=chr(randint(0,127))
    gmail_user = 'sender@gmail.com'
    gmail_app_password = 'app password'
    sent_from = gmail_user
    sent_to = ['reciever@gmail.com', 'reciever@gmail.com']
    sent_subject = "Your New Password"
    sent_body = (output)
    email_text = sent_body
    try:
      server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
      server.ehlo()
      server.login(gmail_user, gmail_app_password)
      server.sendmail(sent_from, sent_to, email_text)
      server.close()
    except Exception as exception:
      print("Error: %s!\n\n" % exception)
if __name__ == '__main__':
    main() 
