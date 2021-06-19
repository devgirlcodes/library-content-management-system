from django.contrib import admin
from .models import *


class BookOrderAdmin(admin.ModelAdmin):
    list_display = ['title','vendor', 'orderNo', 'orderDate', 'orderStatus']
    search_fields = ['title','vendor__name', 'orderNo', 'orderStatus']
    list_filter = ['vendor__name', 'orderStatus']

class BookSuggestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price']
    list_filter = ['price', 'title', 'author']

class AddVendorAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone']

admin.site.register(Genre)
admin.site.register(AddVendor, AddVendorAdmin)
admin.site.register(BookSuggestion, BookSuggestionAdmin)
admin.site.register(BookOrder, BookOrderAdmin)
