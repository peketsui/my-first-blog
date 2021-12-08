from django.urls import path, include
from django.conf.urls import url
from .views import ListTodo, DetailTodo
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('<int:pk>/', DetailTodo.as_view()),
    path('', ListTodo.as_view())
]
