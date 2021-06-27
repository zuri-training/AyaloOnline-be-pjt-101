from django.urls import path
from .views import ListCategory, DetailCategory, ListProduct, DetailProduct
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('categories', ListCategory.as_view(), name='categories'),
    path('categories/<int:pk>/', DetailCategory.as_view(), name='category-detail'),
    path('product', ListProduct.as_view(), name='product'),
    path('product/<int:pk>/', DetailProduct.as_view(), name='product-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)
