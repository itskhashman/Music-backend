import graphene
from music.models import Album
from .types import AlbumType


class AlbumQuery(graphene.ObjectType):
    albums = graphene.List(AlbumType)
    album = graphene.Field(AlbumType, id=graphene.ID(required=True))

    albums_by_artist = graphene.List(AlbumType, artist_id=graphene.ID(required=True))

    def resolve_albums(root, info):
        return Album.objects.all()

    def resolve_album(root, info, id):
        return Album.objects.get(pk=id)

    def resolve_albums_by_artist(root, info, artist_id):
        return Album.objects.filter(artist_id=artist_id)
