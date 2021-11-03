from django.db import models


# Create your models here.
class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class MidiFile(models.Model):
    midi = models.FileField()
    midi_data = models.BinaryField(null=True)
