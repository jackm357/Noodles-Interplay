from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from midi.midifile import MidiInserter
from django.http import HttpResponseRedirect
import mimetypes
import subprocess
from django.db import connection
from midi.models import MidiFile

# example view
def main(request):
    username = request.user.get_username()
    results = MidiFile.objects.all().filter(user=username)
    if request.method == "POST":
        print(request.POST.get("idNum"))
        print(username)
        requested_id = str(request.POST.get("idNum"))
        cursor = connection.cursor()
        subprocess.call(["mkdir", "-p", "/tmp/"+username])
        subprocess.call(["chmod", "777", "/tmp/"+username])
        cursor.execute("COPY (SELECT encode(midi_midifile.midi_data, 'hex') FROM midi_midifile WHERE id = "+requested_id+") TO '/tmp/"+username+"/id"+requested_id+"_out.hex'")
        subprocess.call(["mkdir", "-p", "/home/ubuntu/dev_env/virtual_env/Noodles-Interplay/interplay/media/generated/users/"+username])
        subprocess.call(["xxd", "-ps", "-r", "/tmp/"+username+"/id"+requested_id+"_out.hex", "/home/ubuntu/dev_env/virtual_env/Noodles-Interplay/interplay/media/generated/users/"+username+"/id"+requested_id+"_out.mid"])
        subprocess.call(["sudo", "rm", "-r", "/tmp/"+username])
        return HttpResponseRedirect('/saved/download')
    return render(request, 'saved.html', {"data" : results})



def download(request):
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
    return render(request, 'downloadShared.html')
