# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer
from django.http import HttpResponse


class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

# Create your views here.
def index(request):
    #return HttpResponse("Hello World このページは投稿のインデックスです。")
    return render(request, 'todo/index.html')
