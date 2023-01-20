# users/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("course-index/", views.course_index, name="course_index"),
    path("course-detail/<int:pk>/", views.course_detail, name="course_detail"),
    path("course-enrollment/<int:pk>/", views.course_enrollment, name="course_enrollment"),
    path("task/<int:pk>/", views.task, name="task"),
]