import email, smtplib, ssl
#ip address for raspberry pi is  10.0.0.241
def send_sms_via_email(number: str, message: str, sender_credentials: tuple,
    subject: str="sent using python", smtp_server ="smtp.gmail.com", smpt_port: int = 465):
    sender_email, email_password = sender_credentials
    #reciever_email = f"{number}@@pcs.rogers.com"
    reciever_email = f"{number}@msg.koodomobile.com"

    email_message = f"Subject:{subject}\nTo:{reciever_email}\n{message}"

    with smtplib.SMTP_SSL(smtp_server, smpt_port, context=ssl.create_default_context()) as email:
        email.login(sender_email, email_password)
        email.sendmail(sender_email, reciever_email, email_message)


def main():
    number = "6479494660"
    message = "first python text"
    sender_credentials = ("pythonscriptsasan@gmail.com", "Istakostovai2345")
    send_sms_via_email(number, message, sender_credentials)

if __name__ == '__main__':
    main()