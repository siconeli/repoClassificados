from django.urls import path
from . import views

urlpatterns = [
    path('entrar/', views.Entrar, name='entrar'),
    path('sair/', views.Sair, name='sair'),
    path('cadastrar/', views.CadastrarUsuario, name='cadastrar_usuario'),
]