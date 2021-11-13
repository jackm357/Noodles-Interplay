from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from .forms import UploadFileForm, UploadMidiForm
from django.shortcuts import redirect
from .generator import MelodyGenerator
from .midifile import MidiInserter
import subprocess
import os


def index(req):
    resp = loader.get_template('midi.html').render({}, req)
    return HttpResponse(resp)


def generate_page(request):
    if request.method == 'POST':

        return HttpResponseRedirect('/midi')
    return render(request, 'generate.html')

def melody_page(request):
    if request.method == 'POST':
        modelType = request.POST.get('model')
        numSteps = request.POST.get('steps')
        note = request.POST.get('note')
        user = request.user.get_username()
        print(user)
        gen = MelodyGenerator(modelType, numSteps, note, user)
        call = gen.buildCall()
        subprocess.call([call], shell=True)
        inserter = MidiInserter(user)
        inserter.insert()
        inserter.deleteFiles()
        print("done")
        return HttpResponseRedirect('/midi')
    return render(request, 'melody.html')


def continue_page(request):
    if request.method == 'POST':
        form = UploadMidiForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_midi = form.save(commit=False)
            uploaded_midi.midi_data = form.cleaned_data['midi'].file.read()
            uploaded_midi.user = request.user.get_username()
            uploaded_midi.name = uploaded_midi.filename()
            uploaded_midi.source = "continue"
            uploaded_midi.save()

            subprocess.call(['rm', '-r', 'media/uploaded/' +request.user.get_username()])
            return redirect('/')
    else:
        form = UploadMidiForm()
    return render(request, 'continue.html', {'form': form})


def interpolate_page(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        files = request.FILES.getlist('midi')
        if form.is_valid():
            for f in files:
                uploaded_midi = UploadMidiForm(midi=f)
                uploaded_midi.midi_data = form.cleaned_data['midi'].file.read()
                uploaded_midi.user = request.user.get_username()
                uploaded_midi.name = uploaded_midi.filename()
                uploaded_midi.source = "interpolate"
                uploaded_midi.save()

                subprocess.call(['rm', '-r', 'media/uploaded' + request.user.get_username])
            return HttpResponseRedirect('/')
    else:
        form = UploadFileForm()
    return render(request, 'interpolate.html', {'form': form})
