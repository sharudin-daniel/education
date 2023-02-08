# users/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("landing-index/", views.landing_index, name="landing_index"),
    path("course-index/", views.course_index, name="course_index"),
    path("course-detail/<int:pk>/", views.course_detail, name="course_detail"),
    path("course-enrollment/<int:pk>/", views.course_enrollment, name="course_enrollment"),
    path("task/<int:pk>/", views.task, name="task"),
    path("task/<int:pk>/save/", views.save_task_view, name="save_task_view"),
    path("task/<int:pk>/data/", views.task_view_questions, name="task_view_questions"),

]