from email.parser import Parser
import poplib

#email = input('Email: ')
email = 'wlcearth@hotmail.com'
#password = input('Password: ')
password = 'adfadf219'
#pop3_server = input('POP3 server: ')
pop3_server = 'outlook.office365.com'

server = poplib.POP3_SSL(pop3_server, port=995)
server.set_debuglevel(1)
print(server.getwelcome().decode('utf-8'))

server.user(email)
server.pass_(password)

print('Messages: %s. Size: %s' % server.stat())
resp, mails, octets = server.list()
print(mails)

index = len(mails)
resp, lines, octets = server.retr(index)

msg_content = b'\r\n'.join(lines).decode('utf-8')
msg = Parser().parsestr(msg_content)

server.quit()
