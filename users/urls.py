
from django.urls import path, include
from users.views import dashboard, register

urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
    path("register/", register, name="register"),
    path("oauth/", include("social_django.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
]