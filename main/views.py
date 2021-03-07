from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth import login
from django import forms
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
        info.append( [tamrin, Ersal] )

    filmha = models.Film.objects.all()

    return render(request, 'student.html', context = {'tamrinha':info, 'filmha':filmha})




class FilmForm(forms.ModelForm):
    class Meta:
        model = models.Film
        fields = '__all__'
        widgets = {
            'file': forms.FileInput(attrs={'accept': 'video/*'}),
        }

def ersal_film(request):

    film_form = FilmForm()
    if request.method == 'POST':
        form = FilmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    filmha = models.Film.objects.all()
    return render(request, 'films.html', context = {'filmha':filmha, 'film_form':film_form})


def nemayesh(request, pk):
    film = models.Film.objects.get(pk = pk)
    return render(request, 'nemayesh.html', context = {'film':film})
