# encoding: utf-8
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(verbose_name='Título', max_length=100)
    content = models.TextField(verbose_name='Conteúdo')
    date = models.DateTimeField(verbose_name='Data', auto_now_add=True)
    author = models.ForeignKey(User, verbose_name='Autor', related_name='posts')

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'post'
        ordering = ['-date']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

class Comment(models.Model):
    content = models.TextField(verbose_name='Comentário')
    date = models.DateTimeField(verbose_name='Data', auto_now_add=True)
    post = models.ForeignKey('Post', related_name='comments', verbose_name='Comentários')
    author = models.CharField(verbose_name='Nome', max_length=100)
    email = models.EmailField(verbose_name='Email')

    def __unicode__(self):
        return self.content

    class Meta:
        db_table = 'comment'
        ordering = ['-date']
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'
