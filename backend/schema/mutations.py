import graphene
from .album.mutations import AlbumMutation
from .artist.mutations import ArtistMutation
from .song.mutations import SongMutation

class Mutation(ArtistMutation, AlbumMutation, SongMutation, graphene.ObjectType):
    pass
