from django.contrib import admin

from tracks.models import Track, Singer, Genre, PlayList, TrackPlaylist


admin.site.register(Track)
admin.site.register(Singer)
admin.site.register(Genre)
admin.site.register(PlayList)
admin.site.register(TrackPlaylist)