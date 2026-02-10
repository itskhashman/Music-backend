import graphene
from music.models import Song
from .types import SongType


class SongQuery(graphene.ObjectType):
    songs = graphene.List(SongType)
    song = graphene.Field(SongType, id=graphene.ID(required=True))

    songs_by_album = graphene.List(SongType, album_id=graphene.ID(required=True))

    def resolve_songs(root, info):
        return Song.objects.all()

    def resolve_song(root, info, id):
        return Song.objects.get(pk=id)

    def resolve_songs_by_album(root, info, album_id):
        return Song.objects.filter(album_id=album_id)
