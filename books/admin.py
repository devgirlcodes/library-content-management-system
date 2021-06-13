from django.contrib import admin
from .models import Genre
from .models import Author
from .models import AddNewBook
from .models import Language

class AddNewBookAdmin(admin.ModelAdmin):
    list_display = ['title','author', 'language']
    search_fields = ['title','author__name', 'genre__name', 'language__name']

admin.site.register(Genre)
admin.site.register(AddNewBook, AddNewBookAdmin)
admin.site.register(Author)
admin.site.register(Language)
