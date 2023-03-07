from django.db import models
from django.conf import settings
from django.db.models.signals import post_save


""" Code adapted from Code Institute's "Django REST" walkthrough. """


class Profile(models.Model):
    """
    Profile model which allows for users
    to create a user profile and store data.
    """
    owner = models.OneToOneField(
        settings.AUTH_USER_MODEL,
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


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            owner=instance
        )


post_save.connect(
    create_profile,
    sender=settings.AUTH_USER_MODEL
)
