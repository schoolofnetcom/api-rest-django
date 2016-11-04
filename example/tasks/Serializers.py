from rest_framework import serializers
from .models import Task, Project

from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):

	class Meta:
		model = Task
		fields = ('id', 'title', 'description', 'status', 'owner')


class UserSerializer(serializers.ModelSerializer):
	tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())

	class Meta:
		model = User
		fields = ('id', 'username', 'tasks')


class ProjectSerializer(serializers.ModelSerializer):
	tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())

	class Meta:
		model = Task
		fields = ('id', 'title', 'description', 'status', 'tasks')
