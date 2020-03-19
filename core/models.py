from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	time_minutes = models.IntegerField()
	ingredients = models.CharField(max_length=255)
	description = models.TextField()

	def __str__(self):
		return self.name
