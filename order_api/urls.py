from django.urls import path, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import OrderView


urlpatterns = [

		re_path('order/<int:pk>/',, OrderView,
         name='Order_view'),	
]		




urlpatterns = format_suffix_patterns(urlpatterns)
