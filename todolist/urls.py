from django.urls import path
from todolist.views import *


# TODO: Implement Routings Here
app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('addtask/', add_task, name='addtask'),
    path('json/', show_todolist_by_json , name='show_todolist_by_json'),
    path('add/', submit_ajax, name='submit_ajax')
]