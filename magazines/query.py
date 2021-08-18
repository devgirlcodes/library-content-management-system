import graphene
from .types import GenreType, MagazineType, PublicationType
from .models import Genre, Publication, AddMagazine

class Query(graphene.ObjectType):
    all_magazines = graphene.List(MagazineType)
    all_genres = graphene.List(GenreType)
    all_publications = graphene.List(PublicationType)
    publication_by_name = graphene.Field(PublicationType, name= graphene.String(required=True))
    magazine_by_magazine_name = graphene.Field(MagazineType, name= graphene.String(required=True))
    
    def resolve_all_magazines(root, info):
        return AddMagazine.objects.select_related("publication").all()

    def resolve_all_genres(root, info):
        return Genre.objects.all()

    def resolve_all_publications(root,info):
        return Publication.objects.all()

    def resolve_magazine_by_magazine_name(root, info, name):
        try:
            return AddMagazine.objects.get(name__iexact=name)
        except AddMagazine.DoesNotExit:
            return Exception('Magazine doesn\'t exist')

    def resolve_publication_by_name(root, info, name):
        try:
            return Publication.objects.get(name__iexact=name)
        except Publication.DoesNotExit:
            return Exception('Publisher doesn\'t exist')
