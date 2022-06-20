from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .forms import IdeaForm


def index(request):
    form = IdeaForm()
    context = {'form': form}
    return render(request, "generator/index.html", context)
