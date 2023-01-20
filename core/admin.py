from django.contrib import admin

from core.models import Course, Chapter, Task


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    pass


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass