from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from core.models import Course, Task, Question, Answer


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

def task_view_questions(request, pk):
    task = Task.objects.get(pk=pk)
    questions = []
    for q in task.question_set.all():
        answers = []
        for a in q.answer_set.all():
            answers.append(a.answer)
        questions.append({str(q): answers})
    return JsonResponse({
        'data':questions
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
        print(questions)

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