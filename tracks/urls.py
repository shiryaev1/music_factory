from django.urls import path

from tracks.views import TracksListView

app_name = 'tracks'

urlpatterns = [
    path('', TracksListView.as_view(), name='tracks-list'),
]