from enum import auto
from django.db import models

class Journallist(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    biography = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        db_table = 'journallists'

class Article(models.Model):
    author           = models.ForeignKey(Journallist, on_delete=models.CASCADE)
    title            = models.CharField(max_length=120)
    description      = models.CharField(max_length=200)
    body             = models.TextField()
    location         = models.CharField(max_length=120)
    publication_date = models.DateField()
    activate         = models.BooleanField(default=True)
    created_at       = models.DateTimeField(auto_now_add=True)
    updated_at       = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author} {self.title}'

    class Meta:
        db_table = 'articles'