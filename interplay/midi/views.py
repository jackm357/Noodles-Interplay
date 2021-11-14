from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from .forms import UploadFileForm, UploadMidiForm
from django.shortcuts import redirect
from .generator import MelodyGenerator
from .midifile import MidiInserter
from json import dumps
import mimetypes
import subprocess
import os


def index(req):
    resp = loader.get_template('midi.html').render({}, req)
    return HttpResponse(resp)

def download_page(request):
    if request.method == 'GET':
        print(request.user.get_username())
        user = request.user.get_username()
        filedir = "media/generated/users/" + user
        filename = subprocess.check_output(['ls', filedir])
        filename = filename.decode('utf-8')
        filename = filename.strip()
        fullpath = filedir + "/" + filename
        f = open(fullpath, 'rb')
        mime_type, _ = mimetypes.guess_type(fullpath)
        response = HttpResponse(f, content_type=mime_type)
        response['Content-Disposition'] = "attatchment; filename=%s" % filename
        return response
    return render(request, 'download.html')

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
        inserter = MidiInserter(user)
        inserter.deleteFiles()
        print(user)
        gen = MelodyGenerator(modelType, numSteps, note, user)
        call = gen.buildCall()
        subprocess.call([call], shell=True)
        inserter.insert()

        return HttpResponseRedirect('/midi/download')
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

            midi = MidiInserter(request.user.get_username())

            noteSeqJSON = dumps(str(midi.toNoteSeq()))

            print(noteSeqJSON)
            subprocess.call(['rm', '-r', 'media/uploaded/' + request.user.get_username()])
            return render(request, 'continue.html', {'data': noteSeqJSON})


            #return HttpResponseRedirect('/midi')
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
