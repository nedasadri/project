from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.home, name = 'home'),
    path('teacher/', views.teacher, name = 'teacher'),
    path('student/', views.student, name = 'student'),
    path('filmha/', views.ersal_film, name = 'ersal_film'),
    path('nemayesh/<int:pk>/', views.nemayesh, name = 'nemayesh'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
