from graphene_django import DjangoObjectType 
from music.models import Song

class SongType(DjangoObjectType):
    class Meta:
        model = Song
        fields = ("id", "title", "duration_seconds", "rate", "created_at", "album")

