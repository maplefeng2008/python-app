from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr

import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

#from_addr = input('From: ')
from_addr = 'wanglichao2002@sina.com'
#password = input('Password: ')
password = 'adfADF219'
#to_addr = input('To: ')
to_addr = 'wlcearth@hotmail.com'
#smtp_server = input('SMTP server: ')
smtp_server = 'smtp.sina.com'

msg = MIMEMultipart()
#msg = MIMEText('hello, send by Python...3', 'plain', 'utf-8')
#msg = MIMEText('<html><body><hi>Hello</h1>' +
#        '<p>send by <a href="https://github.com/maplefeng2008">wang</a>...</p>' +
#        '</body></html>', 'html', 'utf-8')

#msg['From'] = from_addr
msg['From'] = _format_addr('wanglc <%s>' % from_addr)
#msg['To'] = to_addr
msg['To'] = _format_addr('haha <%s>' % to_addr)
#msg['Subject'] = 'python send mail'
msg['Subject'] = Header(' python send mail5', 'utf-8').encode()

#msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"</p>' +
    '</body></html>', 'html', 'utf-8'))

with open('./test.png', 'rb') as f:
    mime = MIMEBase('image', 'png', filename='test.png')
    mime.add_header('Content-Disposition', 'attachment', filename='test.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)


print('connecting to smtp server...')
server = smtplib.SMTP(smtp_server, 25)
print('connected!')
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
print('send mail complete!')
server.quit()
