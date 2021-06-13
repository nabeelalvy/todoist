from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from todoit.models import Todoit, Section
# Create your views here.


@login_required()
def home_page(request):
    if request.user.is_authenticated:

        todoit = Todoit.objects.filter(is_completed=False)

        context = {'todoit': todoit}
        return render(request, 'todoit/home.html', context)
    else:
        context = {}
        return render(request, 'todoit/login.html', context)


@login_required()
def add_page(request):
    if request.user.is_authenticated:
        if request.POST:
            task_name = request.POST['task_name']
            if request.POST.get('section_id', default=None) is not None:
                section_id = request.POST['section_id']
                section = Section.objects.get(id=section_id)
                task = Todoit(task_name=task_name, section=section)
                task.save()
            else:
                task = Todoit.objects.create(task_name=task_name)
                print(task)
                task.save()
        # context = {'todoit': None}
        return render(request, 'todoit/add.html')
    else:
        context = {}
        return render(request, 'todoit/login.html', context)


@login_required()
def edit_task_page(request, id):
    if request.user.is_authenticated:
        if request.POST:
            task_name = request.POST['task_name']
            if request.POST.get('section_id', default=None) is not None:
                # section_id = request.POST['section_id']
                # section = Section.objects.get(id=section_id)
                task = Todoit.objects.get(id=id)
                task.task_name = task_name
            else:
                task = Todoit.objects.get(id=id)
                task.task_name = task_name
            task.save()
        else:
            todoit = Todoit.objects.get(id=id)
            context = {'todoit': todoit}
            return render(request, 'todoit/add.html', context)

        return render(request, 'todoit/add.html')
    else:
        context = {}
        return render(request, 'todoit/login.html', context)


@login_required()
def add_section(request):
    if request.user.is_authenticated:
        if request.POST:
            section_name = request.POST['section_name']
            section = Section(section_name=section_name)
            section.save()
        return render(request, 'todoit/add.html')
    else:
        context = {}
        return render(request, 'user_reg/login.html', context)


@csrf_exempt
def task_done(request):
    task_id = request.POST.get('task_id', None)
    task_response = ''
    if task_id is not None:
        task = Todoit.objects.get(id=task_id)
        if task.is_completed is False:
            task.is_completed = True
            task.save()
            task_response = 'Task is marked as done'
        else:
            task_response = 'Task is Already Done'

        print(task_response)
        data = {
            'task': task_response
        }
        return JsonResponse(data)