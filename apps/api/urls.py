from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.api.views import NoteViewSet

router = DefaultRouter()
router.register('notes', NoteViewSet)

# notes/
# notes/<id>/

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
] + router.urls
