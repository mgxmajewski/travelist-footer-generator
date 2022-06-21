from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import FileResponse
from html2image import Html2Image

from .forms import IdeaForm


def index(request):
    form = IdeaForm()
    context = {'form': form}
    return render(request, "generator/index.html", context)


def download(request):
    user_idea = request.POST.get('user_idea')
    print(user_idea)
    phrase = {'phrase': user_idea}
    content = render_to_string('generator/image.html', phrase)
    hti = Html2Image(custom_flags=['--disable-gpu'])
    hti.screenshot(html_str=content, size=(600, 200), save_as='generated-footer.png')
    img = open('./generated-footer.png', 'rb')
    response = FileResponse(img)
    return response
