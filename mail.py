import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import argparse
from gui_util import update_ui_message

parser = argparse.ArgumentParser()
parser.add_argument(
    "--email_username", required=True, help="email username to send from"
)
parser.add_argument(
    "--email_password", required=True, help="email password to send from"
)
args = parser.parse_args()

# A function that sends the email of the result to hadas.c@velismedia.com.
def sendemail(message):
    update_ui_message("Sending email...")

    msg = MIMEMultipart()
    msg["From"] = "or50002001@gmail.com"
    msg["To"] = "hadas.c@velismedia.com"
    msg["Subject"] = "Finished The Program"
    msg.attach(MIMEText(message))

    mailserver = smtplib.SMTP("smtp.gmail.com", 587)
    # identify ourselves to smtp gmail client
    mailserver.ehlo()
    # secure our email with tls encryption
    mailserver.starttls()
    # re-identify ourselves as an encrypted connection
    mailserver.ehlo()
    mailserver.login(args.email_username, args.email_password)

    mailserver.sendmail(
        "or50002001@gmail.com", "hadas.c@velismedia.com", msg.as_string()
    )
    update_ui_message("Email sent!")
