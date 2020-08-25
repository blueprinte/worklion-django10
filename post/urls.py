from django.urls import path
from . import views

app_name="post"

urlpatterns = [
	path('new/', views.new, name='new'),
	path('lists/', views.lists, name='lists'),
	path('<int:post_id>/', views.detail, name='detail'),
	path('create/', views.create, name='create'),
	path('<int:post_id>/edit/', views.edit, name='edit'),
	path('<int:post_id>/update/', views.update, name='update'),
	path('<int:post_id>/delete/', views.delete, name='delete'),
	path('commentcreate/<int:post_id>/', views.commentcreate, name='commentcreate'),
	path('<int:post_id>/like/', views.like, name='like'),
]