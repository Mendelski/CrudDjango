from django.db import models

class Livro(models.Model):
   nome = models.CharField(max_length=100)
   autor= models.CharField(max_length=100)
   edicao = models.IntegerField()

   def __str__(self):
       return self.nome