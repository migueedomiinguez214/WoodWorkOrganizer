import os
from django.contrib.auth.models import Group
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver

def write_email_to_file(subject, message):
    file_path = '/home/migueedomiinguez/Escritorio/bakerydemocopia/bakerydemo/blog/welcome_emails.txt'
    with open(file_path, 'a') as f:
        f.write(f'Subject: {subject}\n')
        f.write(f'Message: {message}\n\n')

@receiver(user_logged_in)
def assign_blogger_group_and_send_welcome_email(sender, user, request, **kwargs):
    Blogger_group = Group.objects.get(name='Blogger')
    if Blogger_group not in user.groups.all():
        user.groups.add(Blogger_group)

        if user.last_login is None:
            subject = 'Nuevo Usuario Añadido'
            message = f'Bienvenido, {user.username}! Has sido añadido a Blogger.'
            write_email_to_file(subject, message)