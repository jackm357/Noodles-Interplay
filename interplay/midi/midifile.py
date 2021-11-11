import subprocess
from django.core.files.base import ContentFile, File
from midi.models import MidiFile
from django.db import models
import os


class MidiInserter:

    user = ""
    dir = "media/generated/melody/users/"

    def __init__(self, user):
        self.user = user



    def insert(self):
        filename = subprocess.check_output(['ls', self.dir + self.user])
        filename = filename.decode('utf-8')
        filename = filename.strip()

        with open(self.dir + self.user + "/" +filename, mode="rb") as f:
            midiModel = MidiFile(midi=filename, midi_data=File(f).read(), user=self.user, source='generated')
            midiModel.save()
            print(filename)

    def deleteFiles(self):
        subprocess.call(['rm', '-r', self.dir + self.user])