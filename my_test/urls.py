from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^user_list/', views.list_user, name='list_user'),
    url(r'^user_create/', views.create_user, name='create_user'),
    url(r'^user_new/', views.new_user, name='new_user'),
]