from django.shortcuts import redirect, render, get_object_or_404, get_list_or_404
# from .forms import RespostaForm
from django.contrib import messages
from .models import Pergunta, Resposta, Categoria, Sub_Categoria


def index(request):

    lista_perguntas = Pergunta.objects.order_by('-data_publicacao')
    categorias = Categoria.objects.all()
    sub_categoria = Sub_Categoria.objects.all() 


    context = {
        'lista_perguntas': lista_perguntas,
        'categorias': categorias,
        'sub_categorias': sub_categoria,
        }

    return render(request, 'polls/index.html', context)


def pergunta_sub_categorias(request, id):

    categorias = Categoria.objects.all()
    sub_categoria = Sub_Categoria.objects.all()

    perguntas = Pergunta.objects.filter(sub_categoria=id)

    context = {
    'perguntas': perguntas,
    'categorias': categorias,
    'sub_categorias': sub_categoria,
    }

    return render(request, 'polls/pergunta-sub-categorias.html', context)



def pergunta_resposta(request, id):

    pergunta = get_object_or_404(Pergunta, id=id)
    categorias = Categoria.objects.all()
    sub_categoria = Sub_Categoria.objects.all()
    # perguntas_sub = Pergunta.objects.filter(sub_categoria=id)

    resposta = request.POST.get('resposta')
    resp = Resposta.objects.filter(pergunta=pergunta).filter(resposta_pergunta=resposta)

    if request.method == 'POST':
        if resp.exists():
            messages.success(request, 'vc acertou')
            print('Você acertou')
        else:
            messages.error(request, 'vc errou, estude mais...')
            print('vc errou')

    context = {
    'perguntas': pergunta,
    'categorias': categorias,
    'sub_categorias': sub_categoria,
    # 'perguntas_sub': perguntas_sub,
    }

    return render(request, 'polls/pergunta_resposta.html', context)


    