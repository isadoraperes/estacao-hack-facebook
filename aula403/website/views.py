from django.shortcuts import render, redirect
from website.models import Pessoa, Ideia

# Create your views here.

def index(request):
    #pag. para cadastrar uma pessoa
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
        context = {'msg' : 'Cadastro realizado com sucesso. Agora insira sua primeira ideia! Acesse com o seu e-mail.'}
        return render(request, 'login.html', context)

    return render(request, 'index.html', context)

def sobre(request):
    # pag. que lista as ideias e seus criadores
    ideias = Ideia.objects.all()
    context = {
        'ideias' : ideias
    }
    return render(request, 'sobre.html', context)

def login(request):
    #pag. confere se existe user cadastrado
    #caso sim, retorna pra pag. sobre
    #caso não, retona pra pag. de cadastro
    #com a msg 'cadastre-se para criar uma ideia'
    if request.method == 'POST':
        email = request.POST.get('email')
        pessoa_bd = Pessoa.objects.filter(email=email_form).first()

        print('Olá, ', pessoa.nome, ' !')

        if pessoa_bd is None:
            #retornar para pag. cadastro
            context = {'msg': 'Cadastra-se para criar uma ideia'}
            return render(request, 'index.html', context)
        else:
            #retorna para pag. de ideias
            context = {'pessoa': pessoa}
            return render(request, 'ideias.html', context)

    return render(request, 'login.html', {})

def cadastrar_ideia(request):
    #renderizar pag. de ideia
    if request.method == 'POST':
        email_pessoa = request.POST.get('email')
        pessoa = Pessoa.objects.filter(email = email_pessoa).first()
        
        if pessoa is not None:
            ideia = Ideia()
            ideia.pessoa = pessoa
            ideia.titulo = request.POST.get('titulo')
            ideia.descricao = request.POST.get('descricao')
            ideia.categoria = request.POST.get('categoria')
            ideia.categoria_outros =  request.POST.get('categoria_outros')
            ideia.save()
            
            print('Ok')
            
            return redirect('/sobre')

    return render(request, 'ideias.html', {})