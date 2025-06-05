from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("comments/", views.comment_list, name="comment_list"),  # GET
    path("post-comment/", views.post_comment, name="post_comment"), 
    
]
