from django.shortcuts import render

# Create your views here.

from .models import Task, Project
from rest_framework import viewsets
from .Serializers import TaskSerializer, UserSerializer, ProjectSerializer

from django.contrib.auth.models import User


class TaskViewSet(viewsets.ModelViewSet):
	queryset = Task.objects.all().order_by('-created')
	serializer_class = TaskSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer

class ProjectViewSet(viewsets.ModelViewSet):
	queryset = Project.objects.all().order_by('-created')
	serializer_class = ProjectSerializer
