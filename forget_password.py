# -*- coding: utf-8 -*-
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from django.utils.encoding import smart_str


def forget_pass(email, username, password):
    try:
        fromaddr = "iransocialnetwork.adm@gmail.com"
        toaddr = email
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = smart_str("recovery password- IRSN")
        body = "dear %s your password is %s" % (username, password)
        msg.attach(MIMEText(smart_str(body), 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, "iransocialnetwork.adm7676")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
        return True
    except:
        return False
#forget_pass("sargdsra@gmail.com", "amir",  "jbdvhbkjdnv")
