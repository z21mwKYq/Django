from django.http import HttpResponse
from django.shortcuts import render
from .models import Bb

# Create your views here.


def index (request):
    bbs = Bb.objects.all()
    return render(request, 'bbroad/index.html', {'bbs':bbs})