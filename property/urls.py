from django.urls import path
from .views import PropertyList

urlpatterns = [
    path(
        'property/',
        PropertyList.as_view()
    ),
]
