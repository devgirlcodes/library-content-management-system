import graphene
from graphene_django import DjangoObjectType
from books.models import Author, Genre, AddNewBook, BookTransaction, Member
from members.models import Member

class AuthorType(DjangoObjectType):
    class Meta:
        model  = Author
        fields = '__all__'

class GenreType(DjangoObjectType):
    class Meta:
        model = Genre
        fields = '__all__'

class BookType(DjangoObjectType):
    class Meta:
        model = AddNewBook
        fields = '__all__'

class BookTrasanctionType(DjangoObjectType):
    class Meta:
        model = BookTransaction
        fields = '__all__'

class MemberType(DjangoObjectType):
    class Meta:
        model = Member
        fields = '__all__'

class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)
    all_authors = graphene.List(AuthorType)
    all_genres = graphene.List(GenreType)
    all_members = graphene.List(MemberType)
    author_by_name = graphene.Field(AuthorType,author_name=graphene.String(required=True))
    book_by_book_title = graphene.Field(BookType,book_title=graphene.String(required=True))
    member_by_member_name = graphene.Field(MemberType,member_name=graphene.String(required=True))


    def resolve_all_books(root,info):
        return AddNewBook.objects.select_related("author").all()

    def resolve_all_authors(root,info):
        return Author.objects.all()
    
    def resolve_all_genres(root,info):
        return Genre.objects.all()
    
    def resolve_all_members(root,info):
        return Member.objects.all()

    def resolve_author_by_name(root,info,author_name):
        try:
            return Author.objects.get(author_name=author_name)
        except Author.DoesNotExist:
            return Exception('Author doesn\'t exist')

    def resolve_book_by_book_title(root,info,book_title):
        try:
            return AddNewBook.objects.get(book_title=book_title)
        except AddNewBook.DoesNotExit:
            return Exception('Book doesn\'t exist')

    def resolve_member_by_member_name(root,self,member_name):
        try:
            return Member.objects.get(member_name=member_name)
        except Member.DoesNotExist:
            return Exception('Member doesn\'t exist')

schema = graphene.Schema(query=Query)

