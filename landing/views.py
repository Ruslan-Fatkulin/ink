from django.shortcuts import render
from .models import *
from .forms import *
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


def home(request):
    slides = Slide.objects.all()
    cards = Card.objects.all()
    categories = Category.objects.all()
    return render(request, 'home.html', {'slides': slides, 'cards': cards,
                                         'categories': categories})


def all(request):
    cards = Card.objects.all()
    return render(request, 'all.html', {'cards': cards})


def application(request):
    form = ApplicationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        form = ApplicationForm()

    return render(request, 'application.html', {'form': form})


def detail(request, pk):
    card = Card.objects.get(pk=pk)
    form = ApplicationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        form = ApplicationForm()
    return render(request, 'detail.html', {'card': card, 'form': form})
