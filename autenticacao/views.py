from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Pessoa, Cargos


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro/index.html')
    elif request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        pessoa = Pessoa(nome=nome, email=email, senha=senha)
        pessoa.save()
        return HttpResponse("Voce foi cadastrado")


def listar(request):
    pessoas = Pessoa.objects.all()
    print(pessoas[0].email)
    return render(request, 'listar/listar.html', {'pessoas': pessoas})
