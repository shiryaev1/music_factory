from django.views.generic import ListView

from tracks.models import Track


class TracksListView(ListView):
    model = Track
    context_object_name = 'tracks'
    template_name = 'tracks/tracks_list.html'

    def get_queryset(self):
        tracks = Track.objects.all()
        return tracks
