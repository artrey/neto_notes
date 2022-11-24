from django.forms import ModelForm

from apps.notes.models import Note


class CreateNoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text', 'is_public']
