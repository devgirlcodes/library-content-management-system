from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Member, Section, Year, Department, MEMBER_TYPE
from books.models import BookTransaction
# Register your models here.

class BookTransactionInline(admin.TabularInline):
    model = BookTransaction
    extra = 0

class MemberAdmin(admin.ModelAdmin):
    def show_issued_books_count(self,obj):
        issued_books_count = BookTransaction.objects.filter(borrower = obj , status = "Issue").count()
        return issued_books_count
    def show_reserved_books_count(self,obj):
        reserved_books_count = BookTransaction.objects.filter(borrower = obj , status = "Reserve").count()
        return reserved_books_count
    def show_returned_books_count(self,obj):
        returned_books_count = BookTransaction.objects.filter(borrower = obj , status = "Returned").count()
        return returned_books_count

    show_issued_books_count.short_description = "Books Issued"
    show_reserved_books_count.short_description = "Books Reserved"
    show_returned_books_count.short_description = "Books Returned"

    list_display = ('card', 'member_name', 'section', 'year', 'member_type', 'department','show_issued_books_count','show_reserved_books_count','show_returned_books_count')
    search_fields = ('card', 'member_name', 'section__sec', 'year__session', 'department__dept', 'member_type')
    list_filter = ("member_type", "section__sec", "year__session", 'department__dept')
    inlines=[BookTransactionInline]

admin.site.register(Member, MemberAdmin)
admin.site.register(Section)
admin.site.register(Year)
admin.site.register(Department)
