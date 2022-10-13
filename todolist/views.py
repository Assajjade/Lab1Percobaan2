import datetime
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from todolist.models import Task
from django.contrib.auth.decorators import login_required
from todolist.forms import addTask


# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    #data_todolist = Task.objects.filter(user = request.user)
    context = {
    # 'todolist': data_todolist,
    'nama': 'Abdillah Assajjad',
    'NPM' : "2106653571",
    'username': request.COOKIES['username'],
    }
    return render(request, "todolist_ajax.html", context)

def submit_ajax(request):
    print('sdasdqwe')
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        new_task = Task(user = request.user, title = title, description = description)
        new_task.save()
    return HttpResponse('')

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('username', username) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')

def add_task(request):
    #print(request.POST)
    
    Task = addTask( request.POST)
    if Task.is_valid():
        Temp = Task.save(commit=False)
        Temp.user = request.user
        Temp.save()
        return HttpResponseRedirect('/todolist')
    context = { 'Task':Task }
    return render(request, 'addtask.html', context)

def show_todolist_by_json(request):
    data = Task.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")