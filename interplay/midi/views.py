from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from .forms import UploadContinueMidiForm, UploadInterpolateMidiForm
from .models import InterpolateUpload
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
        form = UploadContinueMidiForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file_continue(form)
            return redirect('/midi')
    else:
        form = UploadContinueMidiForm()
    return render(request, 'continue.html', {'form': form})

# This callback function handles logic on the interpolate sequence page
def interpolate_page(request):
    if request.method == 'POST':
        form = UploadInterpolateMidiForm(request.POST, request.FILES)
        files = request.FILES.getlist('midi')
        if form.is_valid():
            handle_uploaded_file_interpolate(form, files)
            return redirect('/midi')
    else:
        form = UploadInterpolateMidiForm()
    return render(request, 'interpolate.html', {'form': form})

# Params
# from - The POST request from the file upload.
# This function can be used to handle all logic associated with a generic midi file upload
# Except for the redirect
def handle_uploaded_file_continue(form):
    uploaded_midi = form.save(commit=False)
    uploaded_midi.midi_data = form.cleaned_data['midi'].file.read()
    uploaded_midi.save()

def handle_uploaded_file_interpolate(form, files):
    for f in files:
        uploaded_midi = InterpolateUpload(midi=f)
        uploaded_midi.midi_data = form.cleaned_data['midi'].file.read()
        uploaded_midi.save()
