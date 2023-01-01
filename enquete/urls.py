from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resposta/<int:id>', views.pergunta_resposta, name='pergunta_resposta'),
    path('pergunta_sub_categorias/<int:id>', views.pergunta_sub_categorias, name='pergunta_sub_categorias')
]