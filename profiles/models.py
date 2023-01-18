from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    owner = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=255,
        blank=True
    )
    bio = models.TextField(
        blank=True
    )
    email = models.EmailField(
        max_length=40,
        blank=True
    )
    telephone = models.CharField(
        max_length=20,
        blank=True
    )
    image = models.ImageField(
        upload_to='images/',
        default='../default_profile_hr9s8z'
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateField(
        auto_now=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"
