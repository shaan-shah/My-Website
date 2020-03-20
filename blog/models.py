from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post (models.Model):
	title=models.CharField(max_length=150)
	content=models.TextField()
	date_posted=models.DateTimeField(default=timezone.now)
	author=models.CharField(max_length=100)
	genre=models.CharField(max_length=100)

	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
		return reverse('post-detail',kwargs={'pk':self.pk})




class AuthorInterview (models.Model):
	AuthorName=models.CharField(max_length=150)
	Interview=models.TextField()
	date_posted=models.DateTimeField(default=timezone.now)
	BookName=models.TextField()
			

class Suscribption(models.Model):
	email_id=models.EmailField(max_length=100)