from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date, timedelta
import uuid
from members.models import Member

class Genre(models.Model):
    genre_name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)', verbose_name='Genre')

    def __str__(self):
        return self.genre_name

class Author(models.Model):
    author_name = models.CharField(max_length=200, verbose_name='Author')

    def __str__(self):
        return self.author_name

class Language(models.Model):
    lang_name = models.CharField(max_length=200, verbose_name='Language')

    def __str__(self):
        return self.lang_name

class Publisher(models.Model):
    publisher_name = models.CharField(max_length=200, verbose_name='Publisher')

    def __str__(self):
        return self.publisher_name

class AddNewBook(models.Model):
    accession = models.PositiveIntegerField(unique=True, verbose_name='Accession ID')
    date_of_entry = models.DateField(default=date.today,  verbose_name='Date of Entry')
    book_title = models.CharField(max_length=200, verbose_name='Title', blank=False)
    alternate_title = models.CharField(max_length=200, verbose_name='Alternate Title')
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    language = models.ForeignKey('Language',on_delete=models.SET_NULL, null=True)
    publisher = models.ForeignKey('Publisher',on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name='New Book'

    def __str__(self):
        return self.book_title


    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

class BookTransaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for book across whole library")
    book = models.ForeignKey('AddNewBook',on_delete=models.PROTECT, null=True)
    date_of_transaction = models.DateField(null=False,blank=False,verbose_name='Date Of Transaction',default=date.today(),editable=True) 
    due_back = models.DateField(null=False, blank=False, verbose_name='Due Back Date:',default=date.today()+timedelta(14), editable=True)
    borrower = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True, blank=True)
    is_renewed = models.BooleanField(default=False,verbose_name="Renewed",editable=True)

    BOOK_STATUS = (
        ('Issue', 'Issue'),
        ('Reserve', 'Reserve'),
        ('Returned', 'Returned')
    )

    status = models.CharField(
        max_length=10,
        choices=BOOK_STATUS,
        blank=True,
        help_text='Book availability')

    class Meta:
        verbose_name = 'Book Transaction'
        ordering = ['due_back']
        unique_together = ('book','borrower','status',)
        unique_together = ('book','borrower')

    def __str__(self):
        return self.book.book_title
