import graphene
from graphene_django import DjangoObjectType
from .models import Genre, Publication, AddMagazine

class GenreType(DjangoObjectType):
    class Meta:
        model = Genre
        fields = '__all__'


class PublicationType(DjangoObjectType):
    class Meta:
        model = Publication
        fields = '__all__'


class MagazineType(DjangoObjectType):
    class Meta:
        model = AddMagazine
        field = '__all__'


class MagazineInput(graphene.InputObjectType):
    id = graphene.ID()
    accessionID = graphene.Int(required = True)
    name = graphene.String(required = True)
    subscription_no = graphene.Int(required = True)
