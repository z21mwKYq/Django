from django.http import HttpResponse
from django.shortcuts import render
from .models import Bb
from .models import Rubric

# Create your views here.


def index (request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    return render(request, 'bbroad/index.html', {'bbs':bbs, 'rubrics':rubrics})

def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric = rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context={'bbs':bbs, 'rubrics':rubrics, 'current_rubric':current_rubric}
    return render(request, 'bbroad/by_rubric.html', context)
