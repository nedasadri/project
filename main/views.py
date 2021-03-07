from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth import login
from . import models

def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username, password = password)
        if user:
            login(request, user)
            redirect('main:home')

    return render(request, 'home.html')

def teacher(request):
    tamrinha = models.Tamrin.objects.all()
    if request.method == 'POST':
        matn = request.POST.get('matn')
        time = request.POST.get('time')
        tamrin = models.Tamrin(matn = matn, time = time)
        tamrin.save()

    return render(request, 'teacher.html', context = {'tamrinha':tamrinha})

def student(request):
    tamrinha = models.Tamrin.objects.all()
    info = []
    for tamrin in tamrinha:
        Ersal = None
        for ersal in tamrin.ersalha.all():
            if ersal.student == request.user:
                Ersal = ersal
                break
        info.append( [homework, upload] )

    filmha = models.Film.objects.all()

    return render(request, 'student.html', context = {'tamrinha':info, 'filmha':filmha})
