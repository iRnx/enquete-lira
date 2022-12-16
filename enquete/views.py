from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Pergunta, Resposta

def index(request):

    lista_perguntas = Pergunta.objects.order_by('-data_publicacao')[:5]
    context = {'lista_perguntas': lista_perguntas}

    return render(request, 'polls/index.html', context)


def resultados(request, question_id):

    resultados = get_object_or_404(Pergunta, pk=question_id)

    # question = Question(pk=question_id)

    return render(request, 'polls/results.html', {'resultados': resultados})


def votar(request, question_id):

    pergunta = get_object_or_404(Pergunta, pk=question_id)
    print(request.POST)


    teste = request.POST.get('teste')
    # print(teste)

    resp = Resposta.objects.filter(pergunta=pergunta).filter(texto_escolha__icontains=teste)
    print(resp, '11111111111111111111')

    if resp.exists():
        print('Você acertou')
    else:
        print('vc errou')



      
    try:
        select_choice = pergunta.resposta_set.get(pk=request.POST['respoosta'])
        # print(select_choice, '5555555555555555555555555555555555555555555555555')
    except KeyError:
        return render(request, 'polls/vote.html', {'pergunta': pergunta, 'error_message': 'deu erro fdp'})

    else:
        select_choice.votar += 1
        select_choice.save()
        return HttpResponseRedirect(reverse('resultados', args=(pergunta.id,)))