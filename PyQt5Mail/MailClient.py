import Ui_logging
import sys
from PyQt5 import  QtWidgets
#from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import *
from email.utils import parseaddr,formataddr
#from email.mime.base import MIMEBase 
import smtplib
import  Ui_MainWIndow
def __format_addr(s):
    name,addr =parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))
def guess_server(user):
    userconfig={'163.com':'pop.163.com', 'qq.com':'pop.qq.com', 'gmail.com':'pop.gmail.com'}
    for i in userconfig:
        if i in user:
            return userconfig[i]

def smtplanding(user, password, to_addr,smtp_server):
    server=smtplib.SMTP(smtp_server,25)
    server.set_debuglevel(0)
    server.login(user,password)
    subject=uiMain.pageone_subject.text()
    if uiMain.pageone_radio_button.isChecked is True:
        msg = MIMEMultipart()
        msg.attach(MIMEText(content,'plain',"utf-8"))
        msg['From'] = __format_addr('source sender:<%s>' % user)
        msg['To'] = __format_addr('To Recever:<%s>' % to_addr)
        msg['Subject'] = Header(subject,'utf-8').encode()
        part =MIMEApplication(open('receivemails.jpg','rb').read())
        part.add_header('Content-Disposition', 'attachment',filename='receivemails')   
        msg.attach(part.encode('utf-8'))
    else:
        msg = MIMEText(content,'plain',"utf-8")
        msg['From'] = __format_addr('source sender:<%s>' % user)
        msg['To'] = __format_addr('To Recever:<%s>' % to_addr)
        msg['Subject'] = Header(subject,'utf-8').encode()
    server.sendmail(user,to_addr,msg.as_string())
    server.close()
def receivemails():
    import test
    get_info()
    receivefunc=test.mylogin_function()
    receivefunc.login_mycount(name,mypass, serName, mailindex)
    file=open('%stest.txt'%mailindex, 'r')
    uiMain.pagetwo_From.setText(next(file))
    uiMain.pagetwo_To.setText(next(file))
    uiMain. pagetwo_time.setText(next(file))
    file.close()
    file=open("%s.txt"%mailindex, 'r')
    mailcontent=''
    for line in file:
        line=line.strip()
        mailcontent=mailcontent+line
    file.close()
    uiMain.pagetwo_textbrowser.setHtml(mailcontent)
    
    
def sendmails():
    get_info()
    to_addr=uiMain.pageone_receiver.text()
    smtplanding(name ,mypass,to_addr,smtp_serName)
def get_info():
    global name, mypass, smtp_serName, mailindex, serName, content
    name =ui.username.text()
    mypass=ui.userpass.text()
    serName=guess_server(name)
    smtp_serName=serName.replace('pop','smtp')
    mailindex=uiMain.pagetwo_lineEdit .text()
    content=uiMain.pageone_text.toPlainText()
def onButtonClikedMain():
    global MainWindow
    global uiMain
    widget.hide()
    MainWindow=QtWidgets.QMainWindow()
    uiMain=Ui_MainWIndow.Ui_MainWindow()
    uiMain.setupUi(MainWindow)
    MainWindow.show()
    name =ui.username.text()
    uiMain.user.setText(name)
    uiMain.pagetwo_lineEdit.returnPressed.connect(receivemails)
    uiMain.pageone_buttonBox.clicked.connect(sendmails)
    
app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()

ui =Ui_logging.Ui_widget()
ui.setupUi(widget)
widget.show()
ui.logbutton.clicked.connect(onButtonClikedMain)

sys.exit(app.exec_())
