from django.shortcuts import render
from .models import *


def home(request):
    slides = Slide.objects.all()
    cards = Card.objects.all()
    categories = Category.objects.all()
    return render(request, 'home.html', {'slides': slides,'cards':cards,
                                         'categories': categories})
