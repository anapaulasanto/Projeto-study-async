from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from .models import Produto


def cadastrar_produto (request):
    if request.method == "GET":
        return render(request , 'cadastrar_produto.html')
    
    elif request.method == "POST":
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        validade = request.POST.get('validade')
        quantidade = request.POST.get('quantidade')

        produto = Produto (
            nome = nome,
            preco = preco,
            validade = validade,
            quantidade = quantidade,
        )

        produto.save()
        return redirect ('/estoque/cadastrar_produto')
    

def listar_produtos (request):
    produtos = Produto.objects.all()
    nome1 = request.GET.get('nome')

    if nome1:
        produtos = produtos.filter(nome__icontains = nome1)
    return render(request, 'listar_produtos.html', {'produtos':produtos})

def deletar_produto (request , id):
    produto = Produto.objects.get(id=id)
    produto.delete()
    return redirect ('/estoque/listar_produtos/')