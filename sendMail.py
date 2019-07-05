from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, fromataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(Header(name, 'utf-8').encode(), addr)

#from_addr = input('From: ')
from_addr = 'wanglichao2002@sina.com'
#password = input('Password: ')
password = 'adfADF219'
#to_addr = input('To: ')
to_addr = 'wlcearth@hotmail.com'
#smtp_server = input('SMTP server: ')
smtp_server = 'smtp.sina.com'

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
#msg['From'] = from_addr
msg['From'] = _format_addr('wanglc <%s>' % from_addr)
#msg['To'] = to_addr
msg['To'] = _format_addr('haha <%s>' % to_addr)
#msg['Subject'] = 'python send mail'
msg['Subject'] = Header(' python send mail', 'utf-8').encode()

print('connecting to smtp server...')
server = smtplib.SMTP(smtp_server, 25)
print('connected!')
#server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
print('send mail complete!')
server.quit()
