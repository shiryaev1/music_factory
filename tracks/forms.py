from django import forms

from tracks.models import PlayList, TrackPlaylist


class PlaylistForm(forms.ModelForm):

    class Meta:
        model = PlayList
        fields = (
            'name',
        )


class TrackPlayListForm(forms.ModelForm):

    class Meta:
        model = TrackPlaylist
        fields = (
            'track',
            'playlist',
        )