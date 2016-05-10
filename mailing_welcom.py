import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

def mailing_welcome(email, username):
    fromaddr = "iransocialnetwork.adm@gmail.com"
    toaddr = email
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "dear %s wellcom to IRSN" % username
    body = "HI %s welcome to IRSN the best social network in the world \n your username is : %s \n this email " \
           "will be used for recovering password " % (username, username)
    msg.attach(MIMEText(body, 'plain'))
    filename = "logo.png"
    attachment = open("logo.png", "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "iransocialnetwork.adm7676")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()


#mailing_welcome("sargdsra@gmail.com", "daus")