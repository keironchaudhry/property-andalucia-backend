from .models import Property

from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase


class PropertyListViewTests(APITestCase):
    def setUp(self):
        self.user_seller = get_user_model().objects.create_user(
            username='joelmiller',
            password='ellieisabad@ss',
            seller_status=True
        )

        self.user = get_user_model().objects.create_user(
            username='tommymiller',
            password='donttellmaria',
            seller_status=False
        )
        self.data = {
            "property_type": "villa",
            "province": "granada",
            "municipality": "alhambra",
            "post_code": "33333",
            "price": 120000,
            "size": 120,
            "bedroom_count": 3,
            "bathrooms_count": 2,
            "description": "ill snipe you down from miles away"
        }

    def test_can_list_property(self):
        Property.objects.create(
            owner=self.user_seller,
            name='my texas home',
            property_type='bungalow',
            province='malaga',
            price=100000,
            size=100,
            bedroom_count=2,
            bathrooms_count=2
        )
        response = self.client.get(
            '/property/'
        )
        count = Property.objects.count()
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            count,
            1
        )

    # https://stackoverflow.com/questions/69525611/
    # Following link helped me identify an issue with JSON format,
    # which is the 'format="json"' found in `self.client.post`
    def test_seller_can_create_property_post(self):
        self.client.login(
            username='joelmiller',
            password='ellieisabad@ss',
        )
        response = self.client.post(
            '/property/create/',
            self.data,
            format="json"
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )
        count = Property.objects.count()
        self.assertEqual(count, 1)

    def test_non_seller_cant_create_property_post(self):
        self.client.login(
            username='tommymiller',
            password='donttellmaria'
        )
        response = self.client.post(
            '/property/create/',
            self.data,
            format="json"
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_non_user_cant_create_property_post(self):
        response = self.client.post(
            '/property/create/',
            self.data,
            format="json"
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )
