from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from .forms import UploadFileForm


def index(req):
    resp = loader.get_template('midi.html').render({}, req)
    return HttpResponse(resp)


def continue_page(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'].name)
            return HttpResponseRedirect('/midi')
    else:
        form = UploadFileForm()
    return render(request, 'continue.html', {'form': form})


def handle_uploaded_file(f):
    print(f)