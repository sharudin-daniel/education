from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from core.models import Course, Task


def course_index(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'course_index.html', context)

@login_required
def course_detail(request, pk):
    course = Course.objects.get(pk=pk)
    context = {
        'course': course
    }
    return render(request, 'course_detail.html', context)

@login_required
def course_enrollment(request, pk):
    course = Course.objects.get(pk=pk)
    context = {
        'course': course
    }
    return render(request, 'course_enrollment.html', context)

@login_required
def task(request, pk):
    task = Task.objects.get(pk=pk)
    context = {
        'task': task,
        'course': task.chapter.course
    }
    return render(request, 'task.html', context)