from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Post

urlpatterns = [
		url(r'^$', ListView.as_view(
								queryset=Post.objects.all().order_by("-date")[:25],
								template_name="blog/blog.html")),

		url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Post,
								template_name='blog/post.html'))
]
#P named group. Captures a particular entity
#pk => primary key. auto incremented
#d => digit . coz primary key is a digit.
#+ => regular expression with python