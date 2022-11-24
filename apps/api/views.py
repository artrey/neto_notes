from django.db.models import Q
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from rest_framework.viewsets import ModelViewSet

from apps.api.serializers import NoteSerializer
from apps.notes.models import Note


class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return []
        return [IsAuthenticated()]

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if user.is_anonymous:
            return qs.filter(is_public=True)
        else:
            return qs.filter(Q(is_public=True) | Q(user=user))

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
