from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from .forms import UploadFileForm
from django.shortcuts import redirect


def index(req):
    resp = loader.get_template('midi.html').render({}, req)
    return HttpResponse(resp)


def generate_page(request):
    if request.method == 'POST':
        return HttpResponseRedirect('/midi')
    return render(request, 'generate.html')


def continue_page(request):
    if request.method == 'POST':
        form = UploadMidiForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_midi = form.save(commit=False)
            uploaded_midi.midi_data = form.cleaned_data['midi'].file.read()
            uploaded_midi.save()
            return redirect('/')
    else:
        form = UploadMidiForm()
    return render(request, 'continue.html', {'form': form})


def interpolate_page(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'].name)
            return HttpResponseRedirect('/midi')
    else:
        form = UploadFileForm()
    return render(request, 'interpolate.html', {'form': form})


def handle_uploaded_file(f):
    print(f)
