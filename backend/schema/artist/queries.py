import graphene
from music.models import Artist
from .types import ArtistType


class ArtistQuery(graphene.ObjectType):
    artists = graphene.List(ArtistType)
    artist = graphene.Field(ArtistType, id=graphene.ID(required=True))

    def resolve_artists(root, info):
        return Artist.objects.all()

    def resolve_artist(root, info, id):
        return Artist.objects.get(pk=id)
