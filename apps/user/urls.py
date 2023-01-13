from django.urls import re_path

from . import views

urlpatterns = [
    re_path('users/(?P<user_id>.*)', views.get_users, name='get_users'),
    re_path('log', views.log, name='log'),
]
