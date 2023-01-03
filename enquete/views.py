from random import shuffle
from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
from .form import RespostaForm
from django.contrib import messages
from .models import Pergunta, Resposta, Categoria, Sub_Categoria


def index(request):

    lista_perguntas = Pergunta.objects.order_by('-data_publicacao')
    categorias = Categoria.objects.all()
    sub_categoria = Sub_Categoria.objects.all() 

    # a = shuffle(lista_perguntas)

    context = {
        'lista_perguntas': lista_perguntas,
        'categorias': categorias,
        'sub_categorias': sub_categoria,
        }

    return render(request, 'polls/index.html', context)


def pergunta_sub_categorias(request, id):

    categorias = Categoria.objects.all()
    sub_categoria = Sub_Categoria.objects.all()

    perguntas_sub_categorias = Pergunta.objects.filter(sub_categoria=id)

    print(perguntas_sub_categorias)

    context = {
    'perguntas_sub_categorias': perguntas_sub_categorias,
    'categorias': categorias,
    'sub_categorias': sub_categoria,
    }

    return render(request, 'polls/pergunta-sub-categorias.html', context)



def pergunta_resposta(request, id):

    pergunta = get_object_or_404(Pergunta, id=id)
    categorias = Categoria.objects.all()
    sub_categoria = Sub_Categoria.objects.all()
    lista_perguntas = Pergunta.objects.order_by('-data_publicacao')

    # Trazer a pergunta que contem a subcategoria em específico.
    pergunta_subcategoria_em_especifico = Sub_Categoria.objects.filter(pergunta=id)
    for c in pergunta_subcategoria_em_especifico:
        perguntas_sub_categorias = Pergunta.objects.filter(sub_categoria=int(c.id))


    resposta = request.POST.get('resposta_pergunta')
    resp = Resposta.objects.filter(pergunta=pergunta).filter(resposta_pergunta=resposta)

    if request.method == 'GET':
        form = RespostaForm()


        context = {
        'lista_perguntass': lista_perguntas,
        'pergunta': pergunta,
        'categorias': categorias,
        'sub_categorias': sub_categoria,
        'form': form,
        'perguntass_sub_categorias': perguntas_sub_categorias,
        
        }

        return render(request, 'polls/pergunta_resposta.html', context)
        
    form = RespostaForm(request.POST)

    if request.method == 'POST':
        if form.is_valid:
            if resp.exists():
                messages.success(request, 'vc acertou')
                print('Você acertou')
            else:
                messages.error(request, 'vc errou, estude mais...')
                print('vc errou')
                

    context = {
    'pergunta': pergunta,
    'categorias': categorias,
    'sub_categorias': sub_categoria,
    'form': form,
    'perguntass_sub_categorias': perguntas_sub_categorias,
    }

    return render(request, 'polls/pergunta_resposta.html', context)


    