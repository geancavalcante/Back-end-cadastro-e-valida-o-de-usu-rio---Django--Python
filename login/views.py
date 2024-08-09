from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.http import HttpResponse
from django.contrib import auth



def criar_usuario(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        users = User.objects.filter(username=username)

        if users.exists():
           messages.add_message(request, constants.ERROR, 'usuário Já Existe!')
           return redirect('/cadastro/criar_usuario/')

        if len(password) < 10:
            messages.add_message(request, constants.ERROR, 'Senha muito  curta!') 
            return redirect('/cadastro/criar_usuario/')    

        elif password != confirm_password:
            messages.add_message(request, constants.ERROR, 'senhas incoerents!')
            return redirect('/cadastro/criar_usuario/')

        user = User.objects.create_user(
            username=username,
            password=password,
            )
        user.save()

        return redirect('/cadastro/login')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(request,username=username, password=password)

        if user:
            return HttpResponse('login feito com suscesso')
        else:
            messages.add_message(request, constants.ERROR, 'Dados incorretos!')
            return redirect('/cadastro/login/')


        
        

