from django.conf.urls import url
from posts import views

app_name = 'posts'

urlpatterns = [
    url(r'^create/', views.create, name='create'),
    url(r'^(?P<pk>[0-9]+)/upvote', views.upvote, name='upvote'),
    url(r'^(?P<pk>[0-9]+)/downvote', views.downvote, name='downvote'),
    url(r'^user/(?P<pk>[0-9]+)', views.user_post, name='user_post'),
    # url(r'^posts/(?P<pk>[0-9]+)', views.deleteview, name='deleteview'),
]
