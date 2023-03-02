from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from django.db import transaction
from .models import UpdatedUser

# https://www.rootstrap.com/blog/registration-and-authentication-in-django-apps-with-dj-rest-auth
# Above link was a great tutorial on how
# to manage custom AbstractUser-made fields


class SellerStatusSerializer(RegisterSerializer):

    seller_status = serializers.BooleanField(
        default=False
    )

    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.seller_status = self.data.get(
            'seller_status'
        )
        user.save()
        return user
