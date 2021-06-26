<<<<<<< HEAD
from django.urls import path
from .views import ListCategory, DetailCategory, ListProduct, DetailProduct
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('categories', ListCategory.as_view(), name='categories'),
    path('categories/<int:pk>/', DetailCategory.as_view(), name='category-detail'),
    path('product', ListProduct.as_view(), name='product'),
    path('product/<int:pk>/', DetailProduct.as_view(), name='product-detail'),

    path('signup/', views.Signup.as_view(), name='signup'),
    path('signup/verify/', views.SignupVerify.as_view(),
         name='authemail-signup-verify'),

    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),

    path('password/reset/', views.PasswordReset.as_view(),
         name='password-reset'),
    path('password/reset/verify/', views.PasswordResetVerify.as_view(),
         name='password-reset-verify'),
    path('password/reset/verified/', views.PasswordResetVerified.as_view(),
         name='password-reset-verified'),

    path('email/change/', views.EmailChange.as_view(),
         name='email-change'),
    path('email/change/verify/', views.EmailChangeVerify.as_view(),
         name='email-change-verify'),

    path('password/change/', views.PasswordChange.as_view(),
         name='password-change'),

    path('users/me/', views.UserMe.as_view(), name='me'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
=======
>>>>>>> 5fae535ab9faf9a9b98ef1f242e69896ef63b07c
