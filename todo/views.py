from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from django.db import IntegrityError
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Task, User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
import json

@login_required
def index(request):
    # Authenticated users view their inbox
    if request.method == "POST":
        task_name = request.POST["task"]
        new_task = Task(user=request.user, task_name=task_name)
        new_task.save()

    all_tasks = Task.objects.filter(user=request.user, completed=False)
    paginator = Paginator(all_tasks, 10)  # Show 10 tasks per page
    page_number = request.GET.get('page')
    tasks_of_the_page = paginator.get_page(page_number)

    context = {
        "tasksOfThePage": tasks_of_the_page
    }
    return render(request, "todo/todo.html", context)

@login_required
def completed_tasks(request):
    completed_tasks = Task.objects.filter(user=request.user, completed=True)
    paginator = Paginator(completed_tasks, 10)  # Show 10 tasks per page
    page_number = request.GET.get('page')
    tasks_of_the_page = paginator.get_page(page_number)

    context = {
        "tasksOfThePage": tasks_of_the_page
    }
    return render(request, "todo/completed_tasks.html", context)

@login_required
def mark_in_progress(request, id):
    task = Task.objects.get(id=id, user=request.user)
    task.completed = False
    task.save()
    return HttpResponseRedirect(reverse("completed_tasks"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "todo/register.html", {
                "message": "Passwords must match."
            })
        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "todo/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "todo/register.html")

def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "todo/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "todo/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

@login_required
def delete_task(request, id):
    task = Task.objects.get(id=id, user=request.user)
    task.delete()
    next_url = request.GET.get('next', reverse("index"))
    return HttpResponseRedirect(next_url)

@login_required
def update_task(request, id):
    task = Task.objects.get(id=id, user=request.user)
    task.completed = True
    task.save()
    return HttpResponseRedirect(reverse("index"))

@csrf_exempt
def edit_task(request, id):
    if request.method == 'POST':
        try:
            task = Task.objects.get(id=id)
            data = json.loads(request.body)
            task.task_name = data['content']
            task.save()
            return JsonResponse({'data': task.task_name})
        except Task.DoesNotExist:
            return JsonResponse({'error': 'Task not found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=400)