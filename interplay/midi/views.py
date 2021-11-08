from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from .forms import UploadFileForm, UploadMidiForm
from django.shortcuts import redirect
from .generator import Generator
import subprocess
import os



# var1 = "BUNDLE_PATH=/home/david/PycharmProjects/Noodles-Interplay/interplay/midi/mono.mag"
# var2 = "CONFIG='mono'"
# var3 =  "melody_rnn_generate "
# var4 = "--config='mono' "
# var5 = "--bundle_file=/home/david/PycharmProjects/Noodles-Interplay/interplay/midi/mono.mag "
# var6 = "--output_dir=/tmp/melody_rnn/generated "
# var7 = "--num_outputs=10 "
# var8 = "--num_steps=128 "
# var9 = "--primer_melody=\"[60]\" "

def index(req):
    resp = loader.get_template('midi.html').render({}, req)
    return HttpResponse(resp)


def generate_page(request):
    if request.method == 'POST':
        print("generating")
        #os.system(var1)
        #os.system(var2)
        subprocess.call([var3+var4+var5+var6+var8+var9],shell=True)
        #os.system('echo $BUNDLE_PATH')
        return HttpResponseRedirect('/midi')
    return render(request, 'generate.html')

def melody_page(request):
    if request.method == 'POST':
        modelType = request.POST.get('model')
        numSteps = request.POST.get('steps')
        note = request.POST.get('note')
        gen = Generator(modelType, numSteps,note)
        call = gen.buildCall()
        #print(call)
        subprocess.call([call], shell=True)
        return HttpResponseRedirect('/midi')
    return render(request, 'melody.html')


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
