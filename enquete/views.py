from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Pergunta, Resposta, Categoria, Sub_Categoria

def index(request):

    lista_perguntas = Pergunta.objects.order_by('-data_publicacao')[:5]
    categorias = Categoria.objects.all()
    sub_categoria = Sub_Categoria.objects.all() 

    context = {
        'lista_perguntas': lista_perguntas,
        'categorias': categorias,
        'sub_categorias': sub_categoria,
        }

    return render(request, 'polls/index.html', context)


def trazer_sub_categorias(request, id):

    # categoria = get_object_or_404(Categoria, id=id)


    # pergunta associada aquela categoria

    pergunta = Pergunta.objects.filter(sub_categoria=id)
    print(pergunta, '55555555555555555555555555555555555555555')

    # outra coisa

    categoria = Categoria.objects.filter(sub_categoria__id=id)
    print(categoria, '77777777777777777777777777777777777777777777')

    # mais uma busca

    sub = Sub_Categoria.objects.filter(categoria=id)

    print(sub, '33333333333333333333333333333333333')
    

    return render(request, 'polls/sub-categorias.html', {'pergunta_categoria': pergunta, 'categoria': categoria, 'sub_categoria': sub})


def perguntas_sub_categorias(request, id):

    pergunta = Pergunta.objects.filter(sub_categoria=id)
    return render(request, 'polls/pergunta-sub-categorias.html', {'pergunta': pergunta})


    

def resultados(request, question_id):

    resultados = get_object_or_404(Pergunta, pk=question_id)

    # question = Question(pk=question_id)

    return render(request, 'polls/results.html', {'resultados': resultados})


def votar(request, question_id):

    pergunta = get_object_or_404(Pergunta, pk=question_id)
    print(request.POST)


    teste = request.POST.get('teste')
    # print(teste)

    resp = Resposta.objects.filter(pergunta=pergunta).filter(resposta_pergunta=teste)
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