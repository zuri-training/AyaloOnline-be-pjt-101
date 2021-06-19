from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views




urlpatterns = [
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
