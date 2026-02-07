import graphene
from backend.schema.song.types import SongType
from music.models import Album, Song


class CreateSong(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        album_id = graphene.ID(required=True)
        duration_seconds = graphene.Int(required=False)
        rate = graphene.Float(required=False)

    song = graphene.Field(SongType)

    def mutate(self, info, title, album_id, duration_seconds=None, rate=0.0):
        album = Album.objects.get(pk=album_id)
        song = Song.objects.create(
            title=title,
            album=album,
            duration_seconds=duration_seconds,
            rate=rate or 0.0,
        )
        return CreateSong(song=song)


class DeleteSong(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    ok = graphene.Boolean()

    def mutate(self, info, id):
        Song.objects.filter(pk=id).delete()
        return DeleteSong(ok=True)


class SongMutation(graphene.ObjectType):
    create_song = CreateSong.Field()
    delete_song = DeleteSong.Field()
