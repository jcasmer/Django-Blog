from django.conf import settings
from django.core.mail import EmailMessage

class Utilites:

    def send_email(request):       
        
        try:
            
            subject = request['name']
            html_msg = request['content']
            from_email = settings.EMAIL_HOST_USER
            to_email = settings.DEFAULT_TO_EMAIL
            msg = EmailMessage(subject, html_msg, from_email, [to_email], reply_to=[request['email']])            
            msg.send()
        except Exception as e:
            return  e