# users/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("course-index/", views.course_index, name="course_index"),
    path("course-detail/<int:pk>/", views.course_detail, name="course_detail"),
]