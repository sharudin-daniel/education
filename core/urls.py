# users/urls.py

from django.urls import path

from core.views import start_page

urlpatterns = [
    path("startpage/", start_page, name="startpage"),

]