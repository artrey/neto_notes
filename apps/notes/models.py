from django.contrib.auth.models import User
from django.db import models


class Note(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='notes',
    )
    title = models.CharField(max_length=100, null=True, blank=True)
    text = models.TextField()
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    favourite_by = models.ManyToManyField(
        User, related_name='favourite_notes',
        db_constraint=[
            models.UniqueConstraint(
                fields=['note_id', 'user_id'],
                name='unique_favourites',
            )
        ],
    )
