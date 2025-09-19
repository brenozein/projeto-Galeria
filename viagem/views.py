from django.shortcuts import render, get_object_or_404, redirect
from .models import Viagens
from django.urls import reverse
from django.core.mail import send_mail
from .forms import ContatoForm


def home(request):
    return render(request, 'viagens/home.html')

def viagem_detail(request, id):
    viagem = get_object_or_404(Viagens, pk=id)
    context={
        'viagem': viagem,
    }
    return render(request, 'viagens/viagem_detail.html', context)

def pesquisar_viagens(request):
    query = request.GET.get('q')
    resultado=[]

    if query:
        resultados = Viagens.objects.filter(title__icontains=query)

    context ={
        'query': query,
        'resultados': resultados,
    }
    return render(request, 'viagens/pesquisa.html', context)

def sobre_nos(request):
    return render(request, 'viagens/sobre_nos.html')

def contato(request):
    if request.method == 'POST':

        form = ContatoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            mensagem = form.cleaned_data['mensagem']

            send_mail(
                f'Mensagem de {nome}',
                f'Mensagem de {nome} ({email}):\n\n{mensagem}', email, ['seu_email_para_receber@exemplo.com'], fail_silently= False
            )

            return redirect(reverse('sucesso'))
    else:
        form = ContatoForm()

    return render(request, 'viagens/contato.html', {'form' : form})

def sucesso(request):
    return render(request, 'viagens/sucesso.html')