from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from .forms import UploadFileForm, UploadMidiForm
from django.shortcuts import redirect
from .generator import MelodyGenerator
from .generator import DrumGenerator
from .generator import Interpolater
from .midifile import MidiInserter
from .models import MidiFile
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
        midi = MidiInserter(user)
        midi.deleteFiles()
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
        inserter.insert("melody")

        return HttpResponseRedirect('/midi/download')
    return render(request, 'melody.html')

def drum_page(request):
    if request.method == 'POST':
        drumType = request.POST.get('model')
        user = request.user.get_username()
        inserter = MidiInserter(user)
        inserter.deleteFiles()
        gen = DrumGenerator(user, drumType)
        call = gen.buildCall()
        subprocess.call([call], shell=True)
        inserter.insert("drums")

        return HttpResponseRedirect('/midi/download')
    return render(request, 'drums.html')

# def continue_page(request):
#     if request.method == 'POST':
#         form = UploadMidiForm(request.POST, request.FILES)
#         if form.is_valid():
#             midi = MidiInserter(request.user.get_username())
#             #subprocess.call(['rm', '-r', '-f', 'media/uploaded ' + request.user.get_username()])
#             midi.deleteFiles()
#             uploaded_midi = form.save(commit=False)
#             uploaded_midi.midi_data = form.cleaned_data['midi'].file.read()
#             uploaded_midi.user = request.user.get_username()
#             uploaded_midi.name = uploaded_midi.filename()
#
#             uploaded_midi.source = "continue"
#             uploaded_midi.save()
#
#             url = uploaded_midi.midi.url
#             url = "http://127.0.0.1:8000" + url
#             print(url)
#
#             noteseq = midi.toNoteSeq()
#
#             noteSeqJSON = dumps(str(noteseq))
#
#             #print(noteSeqJSON)
#             midi.deleteFiles()
#             return render(request, 'continue.html', {'data': noteSeqJSON})


            #return HttpResponseRedirect('/midi')
    # else:
    #     form = UploadMidiForm()
    # return render(request, 'continue.html', {'form': form})


def interpolate_page(request):
    if request.method == 'POST':
        form = UploadMidiForm(request.POST, request.FILES)
        files = request.FILES.getlist('midi')
        modelType = request.POST.get('model')
        inserter = MidiInserter(request.user.get_username())
        inserter.deleteFiles()
        filesArr = ["", ""]
        i = 0
        if form.is_valid():
            for f in files:
                uploaded_midi = MidiFile(midi=f)
                uploaded_midi.midi_data = form.cleaned_data['midi'].file.read()
                uploaded_midi.user = request.user.get_username()
                uploaded_midi.name = uploaded_midi.filename()
                uploaded_midi.source = "interpolate-upload"
                uploaded_midi.save()
                filesArr[i] = uploaded_midi.filename()
                i = 1


            interpolate = Interpolater(request.user.get_username(), modelType, filesArr[0], filesArr[1])
            interpolate.buildCall()
            subprocess.call([interpolate.buildCall()], shell=True)
            inserter = MidiInserter(request.user.get_username())
            inserter.insert("interpolation")
            #subprocess.call(['rm', '-r', 'media/uploaded/' + request.user.get_username()])
            return HttpResponseRedirect('/midi/download')
    else:
        form = UploadMidiForm()
    return render(request, 'interpolate.html', {'form': form})


