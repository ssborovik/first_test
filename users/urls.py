from . import views
from django.urls import path, include
from django import contrib

app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('test/', views.MyLogoutView.as_view(), name='test')

]