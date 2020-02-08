from django.urls import path

from tracks.views import TracksListView, PlayListCreateView, TrackPlayListView

app_name = 'tracks'

urlpatterns = [
    path('', TracksListView.as_view(), name='tracks-list'),
    path('playlist/create/', PlayListCreateView.as_view(), name='playlist-create'),
    path('add/track/playlist', TrackPlayListView.as_view(), name='add-track-to-playlist'),
]