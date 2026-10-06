from django.contrib.auth import login
from django.shortcuts import render, get_object_or_404, redirect

from .forms import CadastroForm
from .models import Produto

from django.contrib import messages

def home_view(request):
    return render(request, 'home.html')

def jogo_view(request):
    produtos = Produto.objects.all()
    return render(request, 'jogo.html', {
        'produtos': produtos
    })

def sobre_view(request):
    return render(request, 'sobre.html')

def perfil_view(request):
    return render(request, 'perfil.html')

def cadastro_view(request):
    if request.user.is_authenticated:
        return redirect('perfil')

    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('perfil')
    else:
        form = CadastroForm()

    return render(request, 'cadastro.html', {'form': form})

def detalhes_jogo_view(request, id):
    produto_banco = get_object_or_404(Produto, id=id)
    return render(request, 'detalhes.html', {
        'produto': produto_banco
    })
