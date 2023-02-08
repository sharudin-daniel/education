from django.contrib import admin

from core.models import Course, Chapter, Task, Question, Answer, CourseComment


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    pass

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass

@admin.register(CourseComment)
class AnswerAdmin(admin.ModelAdmin):
    pass