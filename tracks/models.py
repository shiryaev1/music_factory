from django.contrib.auth.models import User
from django.db import models


class Track(models.Model):
    title = models.CharField(max_length=100)
    singer = models.ForeignKey('Singer', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    music = models.FileField(upload_to='upload_tracks/')

    def __str__(self):
        return self.title


class Singer(models.Model):
    name = models.CharField(max_length=50, blank=True)
    surname = models.CharField(max_length=50, blank=True)
    nickname = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nickname


class Genre(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class PlayList(models.Model):
    name = models.CharField(max_length=64)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return f'Playlist {self.name}, created - {self.user.username}'


class TrackPlaylist(models.Model):
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    playlist = models.ForeignKey(PlayList, on_delete=models.CASCADE)

    def __str__(self):
        return f'Track {self.track.title} added to {self.playlist.name} playlist'




