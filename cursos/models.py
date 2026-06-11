from django.db import models
# tabela do banco
class Curso(models.Model):
    nome = models.CharField(max_length=40)
    carga_horaria = models.IntegerField()
    data_criacao = models.DateTimeField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
