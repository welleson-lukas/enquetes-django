from django.urls import path

from . import views

app_name = 'enquete'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:questao_id>/', views.detalhes, name='detalhes'),
    path('<int:questao_id>/resultados/', views.resultados, name='resultados'),
    path('<int:questao_id>/vote/', views.vote, name='vote'),
    path('resultadodata/<str:obj>', views.resultadosData, name='resultadodata')
]