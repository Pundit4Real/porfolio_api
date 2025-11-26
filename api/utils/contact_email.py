from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from datetime import datetime


def send_contact_message(name, email, subject, message, phone=None, service=None):
    """
    Send styled contact message email to the admin inbox.
    """
    html = render_to_string(
        "contacts/contact_email.html",
        {
            "name": name,
            "email": email,
            "subject": subject,
            "message": message,
            "phone": phone,
            "service": service or "Not specified",
            "year": datetime.now().year,
        }
    )

    admin_email = getattr(settings, "ADMIN_EMAIL", None)
    if not admin_email:
        return  # Prevents crash if admin email missing

    email_message = EmailMultiAlternatives(
        subject=f"Portfolio Contact — {name}",
        body="",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[admin_email],
    )
    email_message.attach_alternative(html, "text/html")
    email_message.send()


def send_contact_success_message(name, email):
    """
    Send a thank-you email to the user after submitting the form.
    """
    html = render_to_string(
        "contacts/contact_success.html",
        {
            "name": name,
            "year": datetime.now().year,
        }
    )

    email_message = EmailMultiAlternatives(
        subject="Thank You For Contacting Me",
        body="",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[email],
    )
    email_message.attach_alternative(html, "text/html")
    email_message.send()


def send_contact_reply_email(contact):
    """
    Send a reply email to the user including their original message.
    """
    html = render_to_string(
        "contacts/contact_reply.html",
        {
            "name": getattr(contact, "name", "Valued Contact"),
            "service": getattr(contact, "service", "Not specified"),
            "message": getattr(contact, "message", ""),
            "reply": getattr(contact, "response_message", ""),
            "year": datetime.now().year,
        }
    )

    email_message = EmailMultiAlternatives(
        subject="Response to Your Message",
        body="",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[contact.email],
    )
    email_message.attach_alternative(html, "text/html")
    email_message.send()
