from django.shortcuts import render
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