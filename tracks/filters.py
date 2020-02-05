import django_filters
from tracks.models import Track


class TracksFilter(django_filters.FilterSet):

    class Meta:
        model = Track
        fields = ('title', 'singer', 'genre', )


