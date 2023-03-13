'''
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import Post

def send_comment_notification(post, comment):
    subject = f'Nouveau commentaire de {comment.name}'
    context = {'post': post, 'comment': comment}
    message = render_to_string('comment_notification.html', context)
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.NOTIFY_EMAIL])'''