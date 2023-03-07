from django.db import models
from django.conf import settings
from property.models import Property

""" Code adapted from Code Institute's "Django REST" walkthrough. """


class Note(models.Model):
    """
    Note model which allows for users
    to leave notes on property objects.
    """
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE
    )
    content = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
