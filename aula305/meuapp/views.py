from django.shortcuts import render

# Create your views here.

def pagina_inicial(request):
    context = {"nome": "cachorro", "cachorros": ["mel", "pipoca", "tobias", "cacau", "bob"]}
    return render(request, 'index.html', context)
