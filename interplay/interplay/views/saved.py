from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from midi.models import MidiFile

# example view
def main(request):
        results=MidiFile.objects.all()
        return render(request, 'saved.html', {"data":results})
