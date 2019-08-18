from django.contrib.auth import login, logout, get_user_model
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404

from . import forms
from . import models

User = get_user_model()


class SignUp(CreateView):
	form_class = forms.UserCreateForm
	success_url = reverse_lazy("login")
	template_name = "mysite/signup.html"


class post_list(ListView):
	model = models.Post
	template_name = 'post_list.html'


class post_detail(DetailView):
	model = models.Post


class CreatePost(LoginRequiredMixin, CreateView):
	fields = ('title', 'photo')
	model = models.Post
	success_url = reverse_lazy('post_list')

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.user = self.request.user
		self.object.save()
		return super().form_valid(form)


class user_posts(ListView):
	model = models.Post
	template_name = "user_post_list.html"

	def get_queryset(self):
		try:
			self.post_user = User.objects.prefetch_related("posts").get(
				username__iexact=self.kwargs.get("username")
			)
		except User.DoesNotExist:
			raise Http404
		else:
			return self.post_user.posts.all()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["post_user"] = self.post_user
		return context


@login_required
def add_comment_to_post(request, pk):
	post = get_object_or_404(models.Post, pk=pk)
	if request.method == "POST":
		form = forms.CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.author = request.user
			comment.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = forms.CommentForm()
	return render(request, 'mysite/comment_form.html', {'form': form})