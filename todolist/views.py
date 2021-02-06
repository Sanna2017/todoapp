from django.shortcuts import render
from .models import Todolist

def index (request):
    todo_items = Todolist.objects.order_by ('id') #todo_items VARIBALE 
    context = {'todo_items' : todo_items} #dictionary
    return render (request, 'todolist/index.html', context)

# Create your views here.
