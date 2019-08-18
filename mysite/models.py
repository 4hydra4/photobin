from django.contrib import auth
from django.db import models
from django.utils import timezone
from django.urls import reverse


class User(auth.models.User, auth.models.PermissionsMixin):
	
	def __str__(self):
		return "@{}".format(self.username)


User = auth.get_user_model()


class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
	title = models.CharField(max_length=200)
	upload_date = models.DateTimeField(default=timezone.now)
	photo = models.ImageField(upload_to='images')

	def __str__(self):
		return self.title

	# def get_absolute_url(self):
	# 	return reverse("post_detail",kwargs={'pk':self.pk})


class Comment(models.Model):
	post = models.ForeignKey('mysite.Post', on_delete=models.CASCADE, related_name='comments')
	author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='writes')
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.text