from django.contrib import admin

# Register your models here.
from .models import Madera
admin.site.register(Madera)

from .models import Cliente
admin.site.register(Cliente)

from .models import Empleado
admin.site.register(Empleado)

from .models import Presupuesto
admin.site.register(Presupuesto)

from .models import Articulo
admin.site.register(Articulo)

############################################

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Usuario

class UsuarioInline(admin.StackedInline):
    model = Usuario
    can_delete = False
    verbose_name_plural = "usuario"


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = [UsuarioInline]


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User)