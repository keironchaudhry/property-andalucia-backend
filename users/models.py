from django.db import models
from django.contrib.auth.models import AbstractUser

# URL: https://www.youtube.com/watch?v=8jyyuBaZwVU
# This tutorial taught me how to inherit and use AbstractUser


class UpdatedUser(AbstractUser):
    """ Custom User model that inherits
    and uses AbstractUser to override
    default Django User model """
    seller_status = models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.username

    def get_seller_status(self):
        return self.seller_status
