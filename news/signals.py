from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Category

@receiver(post_save, sender=Category)
def notify_users_post(sender, instance, created, **kwargs):
    if created:
        subject = f'New post in {instance.article_text}'
    else:
        subject = f'Post changed for{instance.article_text}'

    send_mail(
        subject = subject,
        message = instance.message,
    )