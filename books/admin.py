from django.contrib import admin
from .models import Genre, Author, AddNewBook, Language, BookTransaction, Publisher


class GenreAdmin(admin.ModelAdmin):
    def show_genre_books_count(self,obj):
        no_of_books = AddNewBook.objects.filter(genre = obj).count()
        return no_of_books
    show_genre_books_count.short_description = "No.Of Books" 
    
    list_display = ["genre_name","show_genre_books_count"]


class AddNewBookInline(admin.TabularInline):
    model = AddNewBook
    extra = 0
    readonly_fields = ["accession","date_of_entry","book_title","alternate_title","author","genre","publisher","language"]


class AuthorAdmin(admin.ModelAdmin):
    def show_author_books_count(self,obj):
        author_books_count = AddNewBook.objects.filter(author = obj).count()
        return author_books_count
    show_author_books_count.short_description = "No.Of Books"

    list_display = ["author_name","show_author_books_count"]
    search_fields = ["author_name",]
    inlines = [AddNewBookInline]

    class Meta:
        ordering = ["show_author_books_count"]


class BookTransactionInline(admin.TabularInline):
    model = BookTransaction
    extra = 0


class BookTrasanctionAdmin(admin.ModelAdmin):
    list_display = ("book","status","borrower","due_back","is_renewed")
    list_filter = ('status','is_renewed','due_back')
    raw_id_fields = ("borrower","book")
    search_fields = ("borrower__member_name","borrower__member_id","book__book_title")


class AddNewBookAdmin(admin.ModelAdmin):
    def book_status(self,obj):
        result = BookTransaction.objects.filter(book = obj).values_list("status", flat=True) 
        index = len(result)
        if index==0:
            return "Available"
        elif index>=2 and (result[index-1]=="Returned" and result[index-2] != "Reserve"):
            return "Available"
        elif index>=2 and (result[index-1]=="Returned" and result[index-2] == "Reserve"):
            return result[index-2]
        elif index>=2 and (result[index-1]=="Issue" and result[index-2] == "Returned"):
            return result[index-1]
        elif index>=2 and (result[index-1]=="Reserve" and result[index-2] == "Returned"):
            return result[index-1]
        elif index==1:
            return result[0]
        else:
            return "{0} | {1}".format(result[index-2],result[index-1])

    def book_borrower(self,obj):
        book_status = BookTransaction.objects.filter(book = obj).values_list("status", flat=True) 
        result = BookTransaction.objects.filter(book=obj).values_list("borrower__member_name",flat=True)
        index = len(book_status)
        if index==0:
            return "None"
        elif index>=2 and (book_status[index-1]=="Returned" and book_status[index-2] != "Reserve"):
            return "None"
        elif index>=2 and (book_status[index-1]=="Returned" and book_status[index-2] == "Reserve"):
            return result[index-2]
        elif index>=2 and (book_status[index-1]=="Issue" and book_status[index-2] == "Returned"):
            return result[index-1]
        elif index>=2 and (book_status[index-1]=="Reserve" and book_status[index-2] == "Returned"):
            return result[index-1]
        elif index == 1:
            return result[0]
        else:
            return "{0} | {1}".format(result[index-2],result[index-1])
    list_display = ['book_title','author', 'language','book_status','book_borrower']
    list_filter = ("genre",)
    search_fields = ['book_title','author__name', 'genre__name', 'language__name']
    inlines = [BookTransactionInline]

admin.site.register(Genre,GenreAdmin)
admin.site.register(AddNewBook, AddNewBookAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(BookTransaction,BookTrasanctionAdmin)
admin.site.register(Language)
admin.site.register(Publisher)
