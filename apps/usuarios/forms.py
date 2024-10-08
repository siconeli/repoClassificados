from django import forms
from django.contrib.auth import forms as contrib_auth_forms
from .models import Usuario

class UserChangeForm(contrib_auth_forms.UserChangeForm):
    class Meta(contrib_auth_forms.UserChangeForm.Meta):
        model = Usuario
    
class UserCreationForm(contrib_auth_forms.UserCreationForm):
    class Meta(contrib_auth_forms.UserCreationForm.Meta):
        model = Usuario

class CadastrarUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'email','telefone', 'password']