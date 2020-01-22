from django.urls import path
from . import views

app_name = 'test_app'

urlpatterns = [
    path('', views.PostsView.as_view(), name='posts'),
]
