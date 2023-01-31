from django.db import models
from django.conf import settings


class Property(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    property_type = models.CharField(
        max_length=30,
        choices=
    )
    street = models.CharField(
        max_length=40,
        null=True,
        blank=True
    )
    municipality = models.CharField(
        max_length=60
    )
    province = models.CharField(
        max_length=20,
        choices=
    )
    post_code = models.CharField(
        max_length=5
    )
    price = models.PositiveIntegerField()
    size = models.PositiveIntegerField()
    bedroom_count = models.PositiveIntegerField(
        blank=False
    )
    bathrooms_count = models.PositiveIntegerField(
        blank=False
    )
    garage = models.BooleanField(
        default=False
    )
    garden = models.BooleanField(
        default=False
    )
    is_south_facing = models.BooleanField(
        default=False
    )
    description = models.TextField()
    image = models.ImageField(
        upload_to='images/',
        default='../default_property_gbwuvw',
        blank=True
    )
    sold = BooleanField(
        default=False
    )
    latitude = models.FloatField(
        blank=True,
        null=True
    )
    longitude = models.FloatField(
        blank=True,
        null=True
    )
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
