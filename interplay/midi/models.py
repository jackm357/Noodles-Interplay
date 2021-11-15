from django.db import models
import os

def user_directory_path(instance, filename):

    return 'uploaded/{0}/{1}'.format(instance.user, filename)

# Create your models here.
class Document(models.Model):

    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class MidiFile(models.Model):

    midi = models.FileField(upload_to=user_directory_path)
    midi_data = models.BinaryField(null=True)
    user = models.CharField(max_length=128, blank=False, default='')
    source = models.CharField(max_length=15, blank=False, default='')
    name = models.CharField(max_length=200, blank=False, default='')

    class Meta:
        db_table="midi_midifile"

    def filename(self):
        return os.path.basename(self.midi.name)
