from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=20)
    country = models.CharField(max_length=30, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=20)
    release_year = models.PositiveIntegerField(null=True, blank=True)
    artist = models.ForeignKey(Artist, related_name="albums", on_delete=models.CASCADE)
    rate = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=20)
    duration_seconds = models.PositiveIntegerField(null=True, blank=True)
    album = models.ForeignKey(Album, related_name="songs", on_delete=models.CASCADE)
    rate = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
