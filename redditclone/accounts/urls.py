from django.conf.urls import url
from accounts import views

app_name = 'accounts'

urlpatterns = [
    url(r'^signup/', views.signup, name='signup'),
    url(r'^login/', views.loginview, name='loginview'),
    url(r'^logout/', views.logoutview, name='logoutview'),
]
