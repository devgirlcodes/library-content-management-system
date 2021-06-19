
from django.db import models 
from datetime import date
from django.core.validators import RegexValidator

class Genre(models.Model):
    genre_name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)', verbose_name='Genre')

    def __str__(self):
        return self.genre_name


class BookSuggestion(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name='Title', help_text='Title of the book to suggest', blank=False)
    author = models.CharField(max_length=200, verbose_name='Author', blank=False)
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    publisher = models.CharField(max_length=200, verbose_name='Publisher')
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price', help_text='Estimate price of the book')
    card = models.CharField(verbose_name="User-Card Number", max_length=20)

    class Meta:
        verbose_name='Book Suggestion'

    def __str__(self):
        return self.title


class AddVendor(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Vendor Name', blank=False)
    address = models.CharField(max_length=200, null=True, blank=True) 
    pin = models.CharField(null=False, validators=[RegexValidator(r'(^|\D)\d{6}($|\D)')], max_length=6, verbose_name="PIN")
    phone = models.CharField(null=False, validators=[RegexValidator(r'\+?\d[\d -]{8,12}\d')], max_length=13, verbose_name="Phone No.", blank=False)
    email = models.EmailField(null=True, blank=True, help_text="abc@xyz.com")

    class Meta:
        verbose_name='Vendor'

    def __str__(self):
        return self.name


class BookOrder(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name='Title', blank=False)
    author = models.CharField(max_length=200, verbose_name='Author', blank=False)
    publisher = models.CharField(max_length=200, verbose_name='Publisher')
    vendor = models.ForeignKey('AddVendor', on_delete=models.SET_NULL, null=True, blank=False)
    cost = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Cost', help_text='Total cost of order')
    quantity = models.PositiveIntegerField(verbose_name='Number of units ordered')
    orderDate = models.DateField(default=date.today, verbose_name='Date of Order', blank=False)
    orderNo = models.CharField(max_length=10, unique=True, blank=False)

    ORDER_STATUS = (('Undelivered', 'Undelivered'),('Delivered', 'Delivered'))
    orderStatus = models.CharField(max_length=50, choices=ORDER_STATUS, default='Undelivered', verbose_name='Order Status')

    class Meta:
        verbose_name='Book Order'

    def __str__(self):
        return self.title
