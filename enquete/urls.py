from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/resultados/', views.resultados, name='resultados'),
    path('<int:question_id>/votar/', views.votar, name='votar'),
    path('sub-categorias/<int:id>', views.trazer_sub_categorias, name='sub_categoria'),
    path('perguntas_sub_categorias/<int:id>', views.perguntas_sub_categorias, name='perguntas_sub_categorias')
]