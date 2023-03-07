from django.conf import settings
from django.db import models

""" Code adapted from Code Institute's "Django REST" walkthrough. """


class Follower(models.Model):
    """
    Follower model which allows for users
    to follow/unfollow other app users.
    """
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='following',
    )
    followed = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='followed',
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'followed']

    def __str__(self):
        return f'{self.owner.username, self.followed.username}'
