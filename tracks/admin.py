from django.contrib import admin

from tracks.models import Track, Singer, Genre


admin.site.register(Track)
admin.site.register(Singer)
admin.site.register(Genre)

