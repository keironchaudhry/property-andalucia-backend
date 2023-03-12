from .models import Property

from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

""" First few tests are adapted from Code Institute's "Django REST" module """


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


class PropertyDetailViewTests(APITestCase):
    def setUp(self):
        joelmiller = get_user_model().objects.create_user(
            username='joelmiller',
            password='ellieisabad@ss',
            seller_status=True
        )
        abbyanderson = get_user_model().objects.create_user(
            username='abbyanderson',
            password='comingforyoujoel',
            seller_status=True
        )
        Property.objects.create(
            owner=joelmiller,
            name='my texas home',
            property_type='bungalow',
            province='malaga',
            price=100000,
            size=100,
            bedroom_count=2,
            bathrooms_count=2
        )
        Property.objects.create(
            owner=abbyanderson,
            name='my wolf home',
            property_type='apartment',
            province='granada',
            price=200000,
            size=70,
            bedroom_count=1,
            bathrooms_count=1
        )

    def test_can_retrieve_property_using_valid_id(self):
        response = self.client.get('/property/1/')
        self.assertEqual(
            response.data["name"],
            "my texas home"
        )
        self.assertEqual(
            response.data["province"],
            "malaga"
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_cant_retrieve_property_using_invalid_id(self):
        response = self.client.get(
            '/property/10/'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND
        )

    def test_user_can_update_property_fields(self):
        response = self.client.get(
            '/property/1/'
        )
        self.assertEqual(
            response.data['province'],
            'malaga'
        )
        self.client.login(
            username='joelmiller',
            password='ellieisabad@ss'
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
            "description": "damn it ellie"
        }
        response = self.client.put(
            '/property/1/',
            self.data,
            format="json"
        )
        property = Property.objects.filter(
            pk=1
        ).first()
        self.assertEqual(
            property.province,
            'granada'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_user_cant_edit_another_users_property_post(self):
        self.client.login(
            username='abbyanderson',
            password='comingforyoujoel'
        )
        self.data = {
            "property_type": "apartment",
            "province": "huelva",
            "municipality": "trafico",
            "post_code": "44355",
            "price": 50000,
            "size": 30,
            "bedroom_count": 1,
            "bathrooms_count": 1,
            "description": "gotcha joel!"
        }
        response = self.client.put(
            '/property/1/',
            self.data,
            format="json"
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_non_user_cant_update_property_post(self):
        self.data = {
            "property_type": "country property",
            "province": "sevilla",
            "municipality": "mucho trafico",
            "post_code": "66788",
            "price": 120000,
            "size": 150,
            "bedroom_count": 2,
            "bathrooms_count": 2,
            "description": "an anonymous randomer"
        }
        response = self.client.put(
            '/property/1/',
            self.data,
            format="json"
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_seller_can_delete_property_post(self):
        self.client.login(
            username='joelmiller',
            password='ellieisabad@ss'
        )
        count = Property.objects.count()
        self.assertEqual(
            count,
            2
        )
        response = self.client.delete(
            "/property/1/"
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        count = Property.objects.count()
        self.assertEqual(
            count,
            1
        )

    def test_seller_cant_delete_another_users_property_post(self):
        self.client.login(
            username='joelmiller',
            password='ellieisabad@ss'
        )
        count = Property.objects.count()
        self.assertEqual(
            count,
            2
        )
        response = self.client.delete(
            "/property/2/"
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_non_user_cant_delete_property_post(self):
        count = Property.objects.count()
        self.assertEqual(
            count,
            2
        )
        response = self.client.delete(
            "/property/1/"
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )
