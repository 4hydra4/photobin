from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
	path('', views.post_list.as_view(), name='post_list'),
	path('post/<int:pk>/', views.post_detail.as_view(), name='post_detail'),
	path('post/create/', views.CreatePost.as_view(), name='create'),
	path('login/', auth_views.LoginView.as_view(template_name="mysite/login.html"), name='login'),
	path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('signup/', views.SignUp.as_view(), name='signup'),
	path('by/<username>/', views.user_posts.as_view(), name='for_user'),
	path('post/<pk>/remove/', views.post_remove, name='post_remove'),
]