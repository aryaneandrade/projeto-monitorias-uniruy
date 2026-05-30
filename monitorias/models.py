from django.db import models
from django.conf import settings

# Create your models here.

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Beneficio(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    

class Monitoria(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data = models.DateField(blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name='categoria_monitoria')
    beneficio = models.ForeignKey(Beneficio, on_delete=models.PROTECT, related_name='beneficio_monitoria')
    vagas = models.PositiveIntegerField(default=1)

    monitor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='monitorias',
    )

    def __str__(self):
        return self.titulo
    
    @property
    def vagas_preenchidas(self):
        return self.inscricoes.count()

    @property
    def vagas_restantes(self):
        return self.vagas - self.vagas_preenchidas

    @property
    def monitoria_lotada(self):
        return self.vagas_preenchidas >= self.vagas


class Inscricao(models.Model):

    id = models.AutoField(primary_key=True)
    monitoria = models.ForeignKey(Monitoria, on_delete=models.CASCADE, related_name='inscricoes')
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['monitoria', 'email'], name='inscricao_unica_monitoria_email')
        ]

    def __str__(self):
        return f'{self.nome} - {self.monitoria.titulo}'
    



