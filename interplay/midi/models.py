from django.db import models


# Create your models here.
class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class ContinueUpload(models.Model):
    midi = models.FileField(upload_to="continue/")
    midi_data = models.BinaryField(null=True)

class InterpolateUpload(models.Model):
    midi = models.FileField(upload_to="interpolate/")
    midi_data = models.BinaryField(null=True)
