from django.contrib import admin
from .models import Genre, Publication, Language, Frequency, AddMagazine

class AddMagazineAdmin(admin.ModelAdmin):
    list_display = ['name', 'language', 'frequency']
    search_fields = ['name', 'genre__name', 'frequency__name']

admin.site.register(Genre)
admin.site.register(Publication)
admin.site.register(Language)
admin.site.register(Frequency)
admin.site.register(AddMagazine, AddMagazineAdmin)
