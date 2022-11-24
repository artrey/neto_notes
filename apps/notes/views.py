from django.shortcuts import render
from django.views.generic import CreateView

from apps.notes.forms import CreateNoteForm
from apps.notes.models import Note


def notes_view(request):
    context = {
        'object_list': Note.objects.all().select_related('user'),
    }
    return render(request, 'notes/list.html', context)


class CreateNoteView(CreateView):
    form_class = CreateNoteForm
    template_name = 'notes/create.html'
    success_url = '/notes/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)
