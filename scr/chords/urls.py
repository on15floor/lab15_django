from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import ChordsInstrumentView, SongView, SongDelete, SongDetailsView

urlpatterns = [
    # Блог
    path('chords/<instrument>', ChordsInstrumentView.as_view(), name='chords'),
    path('chords/song/create', login_required(SongDetailsView.as_view()), name='song_create'),
    path('chords/song/<song_id>', SongView.as_view(), name='song'),
    path('chords/song/<song_id>/update', login_required(SongDetailsView.as_view()), name='song_update'),
    path('chords/song/<song_id>/del', login_required(SongDelete.as_view()), name='song_delete'),
]
