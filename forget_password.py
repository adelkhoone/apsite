import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
 
def forget_pass(email, username, password):
    fromaddr = "alialirezaamirap@gmail.com"
    toaddr = email
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "recovery password- IRSN"
    body = "dear %s your password is %s" % (username, password)
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "alialirezaamirap7676")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

forget_pass("sargdsra@gmail.com", "amir",  "jbdvhbkjdnv")