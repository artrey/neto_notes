from django.urls import path, include

urlpatterns = [
    path('', include('django_registration.backends.one_step.urls')),
    path('', include('django.contrib.auth.urls')),
]
