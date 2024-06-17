from django.urls import path

from .views import register, get_current_user, update_user

from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("account/register/", register, name="register"),
    path("account/token/", TokenObtainPairView.as_view()),
    path("account/me/", get_current_user, name="me"),
    path("account/me/update/", update_user, name="update_user")
]
