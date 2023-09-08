from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_otp_email(auth_code, email):
    subject = 'Welcome!!!'
    message = f'Your authentication code is: {auth_code}'
    send_mail(subject, message, 'varvar1987a@mail.ru', [email], fail_silently=False)


