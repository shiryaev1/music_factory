from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from tracks.filters import TracksFilter
from tracks.forms import PlaylistForm, TrackPlayListForm
from tracks.models import Track, PlayList, TrackPlaylist


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


class PlayListCreateView(CreateView):
    model = PlayList
    form_class = PlaylistForm
    template_name = 'tracks/playlist_create.html'
    success_url = reverse_lazy('tracks:playlist-create')

    def form_valid(self, form):
        if form.is_valid():
            form.instance.user = self.request.user
            form.save()
        return super().form_valid(form)


class TrackPlayListView(CreateView):
    model = TrackPlaylist
    form_class = TrackPlayListForm
    template_name = 'tracks/track_playlist_create.html'
    success_url = reverse_lazy('tracks:add-track-to-playlist')

