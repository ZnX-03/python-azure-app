from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Curso
from datetime import datetime


@login_required
def listar_cursos(request):
    cursos = Curso.objects.all()
    nome_filtrar = request.GET.get('nome_filtrar')
    carga_horaria_filtrar = request.GET.get('carga_horaria_filtrar')

    if nome_filtrar:
        cursos = cursos.filter(nome__contains=nome_filtrar)
    if carga_horaria_filtrar:
        cursos = cursos.filter(carga_horaria__gte=carga_horaria_filtrar)

    return render(request, 'listar_cursos.html', {'cursos': cursos})


@login_required
def criar_curso(request):
    if request.method == "GET":
        status = request.GET.get('status')
        return render(request, 'criar_curso.html', {'status': status})
    elif request.method == "POST":
        nome_entrada = request.POST.get('nome')
        carga_horaria_entrada = request.POST.get('carga_horaria')
        curso = Curso(
            nome=nome_entrada,
            carga_horaria=carga_horaria_entrada,
            data_criacao=datetime.now()
        )
        curso.save()
        return redirect('/cursos/criar_curso/?status=1')


@login_required
def editar_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)

    if request.method == "GET":
        status = request.GET.get('status')
        return render(request, 'editar_curso.html', {'curso': curso, 'status': status})

    elif request.method == "POST":
        curso.nome = request.POST.get('nome')
        curso.carga_horaria = request.POST.get('carga_horaria')
        ativo_val = request.POST.get('ativo')
        curso.ativo = True if ativo_val == 'true' else False
        curso.save()
        return redirect(f'/cursos/editar_curso/{curso_id}/?status=1')


@login_required
def excluir_curso(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)

    if request.method == "POST":
        curso.delete()
        return redirect('/cursos/listar_cursos/?status=deleted')

    return render(request, 'confirmar_exclusao.html', {'curso': curso})
