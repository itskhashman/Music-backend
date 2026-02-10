from graphene_django import DjangoObjectType 
from music.models import Album


class AlbumType(DjangoObjectType):
    class Meta:
        model = Album
        fields = ("id", "title", "release_year", "rate", "created_at", "artist")
