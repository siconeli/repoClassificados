from django.shortcuts import render, redirect 
from django.urls import reverse

def Inicio(request):
    if request.method == 'GET':
        return render(request, 'core/inicio.html')


        
    