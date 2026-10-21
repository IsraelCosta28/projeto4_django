from django.db import models

class Generos(models.Model):
    nome = models.CharField(max_length=255)  # nome do filme
    
    def __str__(self):
       return self.nome  # representação em string do filme


class Filmes(models.Model):
    
    
   titulo = models.CharField(max_length=255)           # título do filme
   descricao = models.CharField(max_length=255)           # descricao do filme
   ano_lancamento = models.PositiveIntegerField()              # ano de lançamento
   genero = models.ForeignKey(Generos, on_delete=models.CASCADE)              # gênero do filme
   duracao = models.PositiveIntegerField()                  # duração do filme

   def __str__(self):
       return self.titulo  # representação em string do livro
