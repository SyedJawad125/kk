from datetime import datetime
from .serializers import UserSerializer
from periodic_emails.settings import EMAIL_HOST_USER
from django.core.mail import send_mail


def birthday_emails():
    serializer_class = UserSerializer
    current_date = datetime.now()

    employees = serializer_class.Meta.model.objects.filter(dob__month=current_date.month, dob__day=current_date.day)

    if employees:
        emails = [employee.email for employee in employees if employee is not None]
        subject = 'Happiest birthday'
        body= '''
                Dear Employee,
                
                We wish you a very happy birthday
        '''
        send_mail(subject,body, EMAIL_HOST_USER, emails, fail_silently=True)

