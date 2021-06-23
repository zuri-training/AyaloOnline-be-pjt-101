# In urls.py

from rest_framework.routers import DefaultRouter
from .MyViewSet import YourCustomViewSet

default_router = DefaultRouter(trailing_slash=False)

default_router.register('phone', YourCustomViewSet, basename='phone')

url_phonenumber_patterns = default_router.urls
