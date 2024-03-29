from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from html2image import Html2Image

from .forms import IdeaForm


def index(request):
    form = IdeaForm()
    context = {'form': form}
    if not request.session.session_key:
        request.session.create()

    return render(request, "generator/index.html", context)


@csrf_exempt
def download(request):
    user_idea = request.POST.get('user_idea')
    print(user_idea)
    print(f'session {request.session.session_key}')
    phrase = {'phrase': user_idea.lower()}
    content = render_to_string('generator/image.html', phrase)
    hti = Html2Image()
    hti.browser.flags = ['--force-color-profile=SRGB', '--disable-gpu', '--no-sandbox', '--default-background-color=0']
    hti.output_path = './generator/static/generator'
    hti.screenshot(html_str=content, size=(600, 200), save_as=f'generated-footer-{request.session.session_key[:5]}.png')
    return redirect(f'/static/generator/generated-footer-{request.session.session_key[:5]}.png')
