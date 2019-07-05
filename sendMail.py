from email.mime.text import MIMEText
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

#from_addr = input('From: ')
from_addr = 'wanglichao2002@sina.com'
#password = input('Password: ')
password = 'adfADF219'
#to_addr = input('To: ')
to_addr = 'wlcearth@hotmail.com'
#smtp_server = input('SMTP server: ')
smtp_server = 'smtp.sina.com'

msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = 'python send mail'

import smtplib
print('connecting to smtp server...')
server = smtplib.SMTP(smtp_server, 25)
print('connected!')
#server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
print('send mail complete!')
server.quit()
