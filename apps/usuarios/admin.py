from django.contrib import admin
from .models import Usuario
from django.contrib.auth import admin as admin_auth_django
from .forms import UserChangeForm, UserCreationForm

@admin.register(Usuario)
class UsuarioAdmin(admin_auth_django.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = Usuario
    fieldsets = admin_auth_django.UserAdmin.fieldsets + (
        ('Dados', {'fields': ('telefone', 'estado', 'cidade')}),
    )
