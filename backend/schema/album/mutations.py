import graphene
from backend.schema.album.types import AlbumType
from music.models import Artist, Album


class CreateAlbum(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        artist_id = graphene.ID(required=True)
        release_year = graphene.Int(required=False)
        rate = graphene.Float(required=False)

    album = graphene.Field(AlbumType)

    def mutate(self, info, title, artist_id, release_year=None, rate=0.0):
        artist = Artist.objects.get(pk=artist_id)
        album = Album.objects.create(
            title=title,
            artist=artist,
            release_year=release_year,
            rate=rate or 0.0,
        )
        return CreateAlbum(album=album)


class DeleteAlbum(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    ok = graphene.Boolean()

    def mutate(self, info, id):
        Album.objects.filter(pk=id).delete()
        return DeleteAlbum(ok=True)


class AlbumMutation(graphene.ObjectType):
    create_album = CreateAlbum.Field()
    delete_album = DeleteAlbum.Field()
