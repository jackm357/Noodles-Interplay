from django import forms
from midi.models import ContinueUpload, InterpolateUpload
from django.forms import ModelForm

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class UploadContinueMidiForm(ModelForm):
    class Meta:
        model = ContinueUpload
        fields = ['midi']

class UploadInterpolateMidiForm(ModelForm):
    class Meta:
        model = InterpolateUpload
        fields = ['midi']
