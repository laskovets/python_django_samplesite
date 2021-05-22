from bboard.models import Bb, Rubric
from django.shortcuts import render
from django.views.generic.edit import CreateView
from bboard.forms import BbForm
from django.urls import reverse_lazy
from rest_framework.viewsets import ModelViewSet
from bboard.serializers import BbSerializer



# Create your views here.
def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {
        'bbs': bbs,
        'rubrics': rubrics
    }
    return render(request, 'bboard/index.html', context)


def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(id=rubric_id)
    context = {
        'bbs': bbs,
        'current_rubric': current_rubric,
        'rubrics': rubrics
    }
    return render(request, 'bboard/by_rubric.html', context)


class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


class BbViewSet(ModelViewSet):
    queryset = Bb.objects.all()
    serializer_class = BbSerializer
