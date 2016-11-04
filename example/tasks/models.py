from __future__ import unicode_literals

from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
	if created:
		Token.objects.create(user=instance)

class Task(models.Model):
	title = models.CharField(max_length=50)
	description = models.CharField(max_length=200)
	created = models.DateTimeField(auto_now_add=True)
	status = models.BooleanField(default=False)
	owner = models.ForeignKey('auth.User', related_name='tasks')
	project = models.ForeignKey('Project', related_name='tasks')

	def __str__(self):
		return "%s" % self.title


class Project(models.Model):
	title = models.CharField(max_length=50)
	description = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	status = models.BooleanField(default=False)

	def __str__(self):
		return "%s" % self.title