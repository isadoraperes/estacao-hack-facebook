from django.shortcuts import render

# tipo o inflar tela no android
# estamos setando qual página será 'aberta' pela rota definida na url
# ou algo assim
# Create your views here.
def index(request):
    return render(request, 'index.html')
