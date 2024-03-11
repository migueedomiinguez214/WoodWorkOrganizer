from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import Group , User
#from bakerydemo.models import User
from django.dispatch import receiver
from django.core.mail import BadHeaderError,send_mail

@receiver(user_logged_in)
def log_user_login(sender, user, **kwargs):
    try:
        grupo = Group.objects.get(name='Blogger')
        usuario = User.objects.get(username=user)
        correo = User.objects.get(username=user).email
    except:
        print(f"ERROR")
        
    if not grupo in usuario.groups.all():
        usuario.groups.add(grupo.id)
        usuario.save()
        
        send_mail(
            'Inicio Sesion',
            f'Has sido añadido a Blogger',
            'miguelangel.peralta.dominguez.alu@iesfernandoaguilar.es',
            [correo],
            fail_silently=False,
        )
    

