from graphene_django import DjangoObjectType # bridge between django models and graphqL Type
from music.models import Artist


class ArtistType(DjangoObjectType):
    class Meta:
        model = Artist
        fields = ("id", "name", "country", "created_at")
