from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import BbForm

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


class BbCreateView(CreateView):
    template_name = 'bbroad/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubric'] = Rubric.objects.all()
        return context
