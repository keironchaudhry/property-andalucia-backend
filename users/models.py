from django.db import models
from django.contrib.auth.models import AbstractUser


class UpdatedUser(AbstractUser):
    seller_status = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.username

    def get_seller_status(self):
        return self.seller_status
