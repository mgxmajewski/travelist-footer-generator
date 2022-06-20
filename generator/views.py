from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    context = {'phrase_to_render': "popo"}
    return render(request, "generator/index.html", context)
