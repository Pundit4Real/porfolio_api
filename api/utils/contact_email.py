from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from datetime import datetime

def send_contact_message(name, email, subject, message, phone=None):
    """Send styled contact message email to the admin inbox."""

    html = render_to_string(
        "contacts/contact_email.html",
        {
            "name": name,
            "email": email,
            "subject": subject,
            "message": message,
            "phone": phone,
            "year": datetime.now().year
        }
    )

    admin_email = getattr(settings, "ADMIN_EMAIL", None)
    if not admin_email:
        return  # prevents crash if admin email missing

    email_message = EmailMultiAlternatives(
        subject=f"Portfolio Contact — {name}",
        body="",
        from_email=settings.DEFAULT_FROM_EMAIL,  # ✅ Fixed
        to=[admin_email],
    )

    email_message.attach_alternative(html, "text/html")
    email_message.send()



def send_contact_success_message(name, email):
    """
    Send a thank-you email to the user who submitted the contact form.
    """
    html_message = render_to_string('contacts/contact_success.html', {
        'name': name,
    })

    email_message = EmailMultiAlternatives(
        subject="Thank You For Contacting Me",
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,  # From portfolio site
        to=[email]  # ✅ Only send to user
    )
    email_message.attach_alternative(html_message, "text/html")
    email_message.send()