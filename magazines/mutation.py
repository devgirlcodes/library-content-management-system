import graphene
from .models import AddMagazine
from .types import MagazineType, MagazineInput

class AddNewMagazine(graphene.Mutation):
    class Arguments:
        input = MagazineInput(required=True)
    
    magazine = graphene.Field(MagazineType)

    def mutate(parent, info, input=None):
        if input is None:
            return AddNewMagazine(magazine=None)
        _magazine = AddMagazine.objects.create(**input)
        return AddNewMagazine(magazine=_magazine)


class Mutation(graphene.ObjectType):
    add_magazine = AddNewMagazine.Field()
