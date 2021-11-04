from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from .forms import UploadFileForm, UploadMidiForm
from django.shortcuts import redirect


def index(req):
    resp = loader.get_template('midi.html').render({}, req)
    return HttpResponse(resp)

# this callback function handles logic on the generate sequence page
def generate_page(request):
    if request.method == 'POST':
        return HttpResponseRedirect('/midi')
    return render(request, 'generate.html')

# This callback function handles logic on the continue sequence page
def continue_page(request):
    if request.method == 'POST':
        form = UploadMidiForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(form)
            return redirect('/midi')
    else:
        form = UploadMidiForm()
    return render(request, 'continue.html', {'form': form})

# This callback function handles logic on the interpolate sequence page
def interpolate_page(request):
    if request.method == 'POST':
        form = UploadMidiForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(form)
            return redirect('/midi')
    else:
        form = UploadFileForm()
    return render(request, 'interpolate.html', {'form': form})

# Params
# from - The POST request from the file upload.
# This function can be used to handle all logic associated with a generic midi file upload
# Except for the redirect
def handle_uploaded_file(form):
    uploaded_midi = form.save(commit=False)
    uploaded_midi.midi_data = form.cleaned_data['midi'].file.read()
    uploaded_midi.save()
