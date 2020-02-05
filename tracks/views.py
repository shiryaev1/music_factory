from django.views.generic import ListView

from tracks.filters import TracksFilter
from tracks.models import Track


class TracksListView(ListView):
    model = Track
    context_object_name = 'tracks'
    template_name = 'tracks/tracks_list.html'

    def get_queryset(self):
        tracks = Track.objects.all()
        return tracks

    def get_context_data(self, **kwargs):
        context = super(TracksListView, self).get_context_data(**kwargs)
        context['filter'] = TracksFilter(self.request.GET,
                                         queryset=self.get_queryset().order_by(
                                              '-id'
                                         ))
        return context
