from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date

class Genre(models.Model):
    name = models.CharField(max_length=20, help_text='Add a genre (e.g. Sports, Travel etc.)', verbose_name='Genre')

    def __str__(self):
        return self.name


class Publication(models.Model):
    name = models.CharField(max_length=200,unique=True, verbose_name='Publication Name')
    email = models.EmailField(max_length=70,blank=True,unique=True)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=20,unique=True, verbose_name='Language')

    def __str__(self):
        return self.name


class Frequency(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='Frequency')

    def __str__(self):
        return self.name


class AddMagazine(models.Model):
    accessionID = models.PositiveIntegerField(unique=True, verbose_name='Accession ID', blank=False)
    date_of_entry = models.DateField(default=date.today, verbose_name='Date of Entry')
    name = models.CharField(max_length=200, unique=True, verbose_name='Name', blank=False)
    genre = models.ManyToManyField(Genre, help_text='Add genre for this magazine')
    language = models.ForeignKey('Language',on_delete=models.SET_NULL, null=True)
    frequency = models.ForeignKey('Frequency',on_delete=models.SET_NULL, null=True)
    publication = models.ForeignKey('Publication',on_delete=models.SET_NULL, null=True)
    subscription_no= models.CharField(max_length=200, unique=True, verbose_name='Subscription Number', null=True)
    subscription_fee = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Subscription Fee', null=True)
    subs_start_date = models.DateField(default=date.today, verbose_name='Subscription starts on')
    subs_end_date = models.DateField(verbose_name='Subscription ends on', null=True)
    
    class Meta:
        verbose_name='Magazine'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('magazine-detail', args=[str(self.id)])
