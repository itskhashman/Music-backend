import graphene
from backend.schema.artist.types import ArtistType
from music.models import Artist


class CreateArtist(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        country = graphene.String(required=False)

    artist = graphene.Field(ArtistType)

    def mutate(self, info, name, country=""):
        artist = Artist.objects.create(name=name, country=country or "")
        return CreateArtist(artist=artist)


class DeleteArtist(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    ok = graphene.Boolean()

    def mutate(self, info, id):
        Artist.objects.filter(pk=id).delete()
        return DeleteArtist(ok=True)


class ArtistMutation(graphene.ObjectType):
    create_artist = CreateArtist.Field()
    delete_artist = DeleteArtist.Field()