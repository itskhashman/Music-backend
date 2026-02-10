import graphene
from .artist.queries import ArtistQuery
from .album.queries import AlbumQuery
from .song.queries import SongQuery

class Query(ArtistQuery, AlbumQuery, SongQuery, graphene.ObjectType):
    pass
