from django.shortcuts import render
from website.models import Pessoa

# Create your views here.

def index(request):
    context = {
        
    }
    if request.method == 'POST':
        pessoa = Pessoa()
        pessoa.nome = request.POST.get('nome')
        pessoa.sobrenome = request.POST.get('sobrenome')
        pessoa.email = request.POST.get('email')
        pessoa.sexo = request.POST.get('sexo')
        pessoa.biografia = request.POST.get('biografia')
        pessoa.save()
        context = {'msg' : 'Cadastro realizado com sucesso.'}

    return render(request, 'index.html', context)

def sobre(request):
    pessoa = Pessoa.objects.all()
    context = {
        'pessoas' : pessoa
    }
    return render(request, 'sobre.html', context)