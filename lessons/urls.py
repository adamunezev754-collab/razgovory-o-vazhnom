from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('documents/', views.documents_list, name='documents'),
    path('class/<str:class_name>/', views.class_lessons, name='class_lessons'),
    path('lesson/<int:pk>/', views.lesson_detail, name='lesson_detail'),
]