from django.db import models
from django.conf import settings


class Blog(models.Model):
    """ Database model for Blog feature """
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=200,
        blank=True
    )
    content = models.TextField(
        blank=True
    )
    image = models.ImageField(
        upload_to='images/',
        default='../default_property_gbwuvw'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.title}'
