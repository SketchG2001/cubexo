from django.template.loader import render_to_string
from django.core.mail import EmailMessage
import logging
from django.conf import settings
import os

logger = logging.getLogger(__name__)

def email_sender(html_template,context):
    file_path = os.path.join(settings.BASE_DIR,'static','img','sample.jpg')
    from_email = settings.DEFAULT_FROM_EMAIL
    subject = context.get('subject')
    to_email = context.get('to_email')
    cc = context.get('cc')
    bcc = context.get('bcc')

    with open(file_path, 'rb') as file:
        img_data = file.read()

    if not to_email:
        raise ValueError("To email required")
    elif not isinstance(to_email,list):
        to_email = [to_email]

    try:
        html_message = render_to_string(html_template,context)
        message = EmailMessage(
            subject=subject,body=html_message,from_email=from_email,to=to_email,cc=cc,bcc=bcc
        )
        message.attach('sample.jpg',img_data,'image/jpeg')
        message.content_subtype = 'html'
        result = message.send()
        print(result)
        logger.info(f"sending email to {','.join(to_email)} with subject - status{result}")
    except Exception as e:
        logger.info(f"Sending email to {', '.join(to_email)} with subject: {subject} - Status 0")
        logger.exception(e)