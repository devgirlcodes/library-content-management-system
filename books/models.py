from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)', verbose_name='Genre')

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200, verbose_name='Author')

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=200, verbose_name='Language')

    def __str__(self):
        return self.name

class AddNewBook(models.Model):
    accession = models.PositiveIntegerField(unique=True, verbose_name='Accession ID')
    date_of_entry = models.DateField(default=date.today,  verbose_name='Date of Entry')
    title = models.CharField(max_length=200, verbose_name='Title', blank=False)
    alternate_title = models.CharField(max_length=200, verbose_name='Alternate Title')
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    publisher = models.CharField(max_length=200, verbose_name='Publisher')
    language = models.ForeignKey('Language',on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name='New Book'

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
