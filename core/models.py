from pathlib import Path

from django.db import models
import os

BASE_DIR = Path(__file__).resolve().parent.parent


class CourseCategory(models.TextChoices):
    ENGLISH = 'English'
    MATH = 'Math'
    OTHER = 'Other'

class Course(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    image = models.FilePathField(path= os.path.join(BASE_DIR, 'static/img'),)
    category = models.CharField(
        max_length=60,
        choices=CourseCategory.choices,
        default=CourseCategory.OTHER,
    )
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    numberOfUsers = models.IntegerField()


class Chapter(models.Model):
    title = models.CharField(max_length=100)
    theoreticatPart = models.TextField()
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    rightAnswer = models.TextField()
    chapter = models.ForeignKey(to=Chapter, on_delete=models.CASCADE)


