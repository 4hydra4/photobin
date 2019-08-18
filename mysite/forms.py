from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from django import forms
from .models import Comment


class UserCreateForm(UserCreationForm):
	class Meta:
		fields = ("username", "email", "password1", "password2")
		model = get_user_model()


class CommentForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = ('text',)