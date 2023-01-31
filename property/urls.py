from django.urls import path
from .views import PropertyListView

urlpatterns = [
    path(
        'property/',
        PropertyList.as_view()
    ),
]
