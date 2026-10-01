from django.shortcuts import render, get_object_or_404
from .models import Produto

# Create your views here.
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


def detalhes_jogo_view(request, id):
    produto_banco = get_object_or_404(Produto, id=id)
    return render(request, 'detalhes.html',{'produto': produto_banco})