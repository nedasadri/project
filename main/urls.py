from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('teacher/', views.teacher, name = 'teacher'),
    path('student/', views.student, name = 'student'),
]
