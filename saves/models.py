from django.db import models
from django.conf import settings
from property.models import Property

""" Code adapted from Code Institute's "Django REST" walkthrough. """


class Save(models.Model):
    """
    Save model which allows for users
    to save/unsave other user property objects.
    """
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    property = models.ForeignKey(
        Property,
        related_name='saves',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'property']

    def __str__(self):
        return f'{self.owner.username, self.property}'
