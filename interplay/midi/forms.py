from django import forms
from midi.models import MidiFile
from django.forms import ModelForm

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class UploadMidiForm(ModelForm):
    class Meta:
        model = MidiFile
        fields = ['midi']
