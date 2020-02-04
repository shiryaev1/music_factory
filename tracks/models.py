from django.db import models


class Track(models.Model):
    title = models.CharField(max_length=100)
    singer = models.ForeignKey('Singer', on_delete=models.CASCADE)
    genre = models.OneToOneField('Genre', on_delete=models.CASCADE)
    music = models.FileField(upload_to='static/media/upload_tracks/')

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
