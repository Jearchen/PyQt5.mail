from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr
import poplib
import os
def decode_str(s):
    value, charset = decode_header(s)[0]
    if charset:
        value = value.decode(charset)
    return value
def guess_charset(msg):
    charset = msg.get_charset()
    if charset is None:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos >= 0:
            charset = content_type[pos + 8:].strip()
    return charset
def print_info(msg, i,indent=0):
    if indent == 0:
        for header in ['From', 'To', 'Subject']:
            value = msg.get(header, '')
            if value:
                if header=='Subject':
                    value = decode_str(value)
                else:
                    hdr, addr = parseaddr(value)
                    name = decode_str(hdr)
                    value = u'%s <%s>' % (name, addr)
            file =open("%stest.txt"%i,"a")
            file.write('%s\n' %value)
            file.close()
    if (msg.is_multipart()):
        parts = msg.get_payload()
        for n, part in enumerate(parts):
            file =open("%s.txt"%i,"a")
            file.write('part %s\n' %n)
            file.close()
            print_info(part,i, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type=='text/plain' or content_type=='text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
                print(content)
            file =open("%s.txt"%i,"a")
            file.write('Text: %s\n' % (content + '...'))
            file.close()
        else:
            file =open("%s.txt"%i,"a")
            file.write('Attachment: %s\n' % (content_type))
            file.close()
class mylogin_function():
    def login_mycount(self, email, password, serName, mailindex):
        server = poplib.POP3(serName)
        server.set_debuglevel(1)
        server.user(email)
        server.pass_(password)
        resp, mails, octets = server.list()
        resp, lines, octets = server.retr(mailindex)
        try:
            msg_content = b'\r\n'.join(lines).decode('utf-8')
            msg = Parser().parsestr(msg_content)        
            print_info(msg,mailindex)
        except:
            print("an error occured")
            #os.remove("%s.txt"%mailindex)
        # server.dele(index)
               # stat()返回邮件数量和占用空间:
        #print('Messages: %s. Size: %s' % server.stat())
        # list()返回所有邮件的编号:
        server.quit()
