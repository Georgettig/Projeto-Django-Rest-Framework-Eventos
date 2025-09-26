from django.db import models

# Create your models here.
class Evento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    local = models.CharField(max_length=100)
    data = models.DateTimeField()

    def __str__(self):
        return self.nome

class Participante(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=13)

    def __str__(self):
        return self.nome

class Inscricao(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='inscricao')
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE, related_name='inscricao')
    data_inscricao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.participante.nome} - {self.evento.nome}"