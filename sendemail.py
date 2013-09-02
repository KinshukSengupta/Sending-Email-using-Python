#!/usr/bin/python
import os,sys
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
def main(argv):
    try:
	email = argv.split(',')[0]
	user = argv.split(',')[1]
	authtoken = argv.split(',')[2]
	msg = MIMEMultipart()
	msg['From'] = 'hive1@gmx.com'
	msg['To'] = argv.split(",")[0]
	msg['Subject'] = 'Password Recovery Email for Hive'
	message = 'Dear User,\n Kindly click in the link to reset your password.\n http://127.0.0.1:8080/resetcheck.jsp?email=%s&user=%s&authtoken=%s\n\nThanks Hive Admin' %(email,user,authtoken)
	msg.attach(MIMEText(message))

	mailserver = smtplib.SMTP('mail.gmx.com')
	mailserver.ehlo()
	#mailserver.starttls()
	mailserver.ehlo()
	mailserver.login('hive1@gmx.com', '1234@)!@')
	mailserver.sendmail('hive1@gmx.com',email,msg.as_string())
	mailserver.quit()
	print "ok"
    except:
        import traceback
	print traceback.format_exc()


if __name__ == "__main__":
    print main(sys.argv[1])
