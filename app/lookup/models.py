from django.db import models


class Word(models.Model):
    word = models.CharField(max_length=100)
    language = models.CharField(max_length=10)
    masc_form = models.CharField(max_length=100, blank=True)
    masc_meaning = models.CharField(max_length=100, blank=True)
    fem_form = models.CharField(max_length=100, blank=True)
    fem_meaning = models.CharField(max_length=100, blank=True)
    neut_form = models.CharField(max_length=100, blank=True)
    neut_meaning = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.word} ({self.language})'


class Spelling(models.Model):
    spelling = models.CharField(max_length=50)
    words = models.ManyToManyField(Word)

    def __str__(self):
        return self.spelling
