from django.shortcuts import render, get_object_or_404
from .models import Viagem

def home(request):
    return render(request, 'viagens/home.html')

def viagem_detail(request, id):
    viagem = get_object_or_404(Viagem, pk=id)
    context={
        'viagem': viagem,
    }
    return render(request, 'viagens/viagem_detail.html', context)

def pesquisar_viagens(request):
    query = request.GET.get('q')
    resultado=[]

    if query:
        resultados = Viagem.objects.filter(title__icontains=query)

    context ={
        'query': query,
        'resultados': resultados,
    }
    return render(request, 'viagens/pesquisa.html', context)