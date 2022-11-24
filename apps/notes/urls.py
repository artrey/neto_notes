from django.urls import path

from apps.notes.views import notes_view, CreateNoteView

urlpatterns = [
    path('', notes_view),
    path('create/', CreateNoteView.as_view()),
]
