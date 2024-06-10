from django.shortcuts import render, redirect 

def Inicio(request):
    if request.method == 'GET':
        return render(request, 'core/inicio.html')

