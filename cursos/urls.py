from django.urls import path
from . import views

urlpatterns = [
    path('listar_cursos/', views.listar_cursos, name='listar_cursos'),
    path('criar_curso/', views.criar_curso, name='criar_curso'),
    path('editar_curso/<int:curso_id>/', views.editar_curso, name='editar_curso'),
    path('excluir_curso/<int:curso_id>/', views.excluir_curso, name='excluir_curso'),
]