'''
import smtplib
from email.mime.text import MIMEText
from django.conf import settings


def send_email(comment):
    sender = 'jscinnamon7483@gmail.com'
    password = 'vmwarehightechcirpi55$'
    recipient = 'jscinnamon7483@gmail.com'
    #creer un message a envoyer
    subject = f'Nouveau commentaire de {comment.name}'
    body = f'{comment.name} a laisser un nouveau commentaire sur votre blog : \n\n{comment.commment}'
    message = MIMEText
    message['subject'] = subject
    message['from'] = sender
    message['to'] = recipient

    #envoyer le message a l'utilisateur SMTP
    server = smtplib.SMTP('smtp.example.com', 587)
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, recipient, message.as_string())
    server.quit()
'''