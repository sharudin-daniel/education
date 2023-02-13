from audioop import reverse

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect

from core.forms import CommentForm
from core.models import Course, Task, Question, Answer, CourseComment, CourseResult, TaskResult, QuestionResult

import logging

logger = logging.getLogger(__name__)
def landing_index(request):
    return render(request, 'landing_index.html')

def course_index(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'course_index.html', context)

def course_detail(request, pk):
    course = Course.objects.get(pk=pk)

    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = 'Anonimus'

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.course = course
            new_comment.author = username
            new_comment.save()
            comments = course.coursecomment_set.all()
            sum = 0
            for comment in comments:
                sum += comment.rating
            course.rating = round(sum / comments.count(), 2)
            course.save()
    else:
        comment_form = CommentForm()

    course_result = CourseResult.objects.filter(user=request.user).filter(course=course)
    if course_result:
        course_result = course_result[0]

    context = {
        'course': course,
        'comment_form': comment_form,
        "course_result": course_result
    }
    return render(request, 'course_detail.html', context)

@login_required
def course_enrollment(request, pk):
    course = Course.objects.get(pk=pk)
    course_result = CourseResult.objects.filter(user=request.user).filter(course=course)
    if not course_result:
        CourseResult.objects.create(course=course, user= request.user, score=0)
    context = {
        'course': course
    }
    return render(request, 'course_enrollment.html', context)

@login_required
def task(request, pk):
    task = Task.objects.get(pk=pk)
    task_result = TaskResult.objects.filter(user=request.user).filter(task=task)
    context = {
        'task': task,
        'course': task.chapter.course,
    }
    logger.warning(task_result)

    if task_result:
        task_result = task_result[0]
        question_results = task_result.questionresult_set.all()
        context.update({"question_results": question_results})
        return render(request, 'task_results.html', context)
    else:
        if request.method == 'POST':
            questions = []
            data = request.POST
            data_ = dict(data.lists())
            data_.pop('csrfmiddlewaretoken')
            for k in data_.keys():
                question = Question.objects.get(description=k)
                questions.append(question)
            question_results = []
            correct_answer = None
            task_result = TaskResult.objects.create(task=task, user=request.user, score=0)
            for q in questions:
                a_selected = request.POST.get(q.description)

                questions_answers = Answer.objects.filter(question=q)
                for a in questions_answers:
                    if a.correct:
                        correct_answer = a.answer
                question_result = QuestionResult.objects.create(question=q, user=request.user, correct_answer=correct_answer,
                                                                    task_result=task_result, given_answer=a_selected)
                question_results.append(question_result)

            # todo: поменять скор (сейчас нолик)
            context.update({"question_results": question_results})
            return render(request, 'task_results.html', context)

        else:
            questions = []
            for q in task.question_set.all():
                answers = []
                for a in q.answer_set.all():
                    answers.append(a.answer)
                questions.append({str(q): answers})
            context.update({"questions": questions})
            return render(request, 'task.html', context)

def task_results(request, pk, context):
    logger.warning("----------task_results----------")

def task_view_questions(request, pk):
    task = Task.objects.get(pk=pk)
    questions = []
    for q in task.question_set.all():
        answers = []
        for a in q.answer_set.all():
            answers.append(a.answer)
        questions.append({str(q): answers})
    return JsonResponse({
        'data': questions
    })

def save_task_view(request, pk):
    if  request.headers.get('x-requested-with') == 'XMLHttpRequest':
        questions = []
        data = request.POST
        data_ = dict(data.lists())
        data_.pop('csrfmiddlewaretoken')
        for k in data_.keys():
            question = Question.objects.get(description=k)
            questions.append(question)

        user = request.user
        task = Task.objects.get(pk=pk)
        score = 0
        # multiplier = 100 / task.number_of_questions
        results = []
        correct_answer = None
        for q in questions:
            a_selected = request.POST.get(q.description)
            if a_selected != "":
                questions_answers = Answer.objects.filter(question=q)
                for a in questions_answers:
                    if a_selected == a.answer:
                        if a.correct:
                            score += 1
                            correct_answer = a.answer
                    else:
                        if a.correct:
                            correct_answer = a.answer
                results.append({str(q): {'correct_answer': correct_answer, 'answered': a_selected}})
            else:
                results.append({str(q): 'not answered'})
        # score_ = score * multiplier
    return JsonResponse({'score':score, 'results':results})