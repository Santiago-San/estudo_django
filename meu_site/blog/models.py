from random import choices
from django.db import models
# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    STATUS = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado'),

    )
    titulo = models.CharField(max_length=250)
    slug   = models.SlugField(max_length=250)
    autor  = models.ForeignKey(User,
                                on_delete=models.CASCADE)
    conteudo = models.TextField()
    publicado = models.DateTimeField(default=timezone.now)
    criado = models.DateTimeField(auto_now_add=True)
    alterado = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS,
                              default='rascunho')

    def __str__(self):
        return self.titulo
    class Meta:
        ordering = ('publicado',)

