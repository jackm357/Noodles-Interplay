import subprocess
from django.core.files.base import ContentFile, File
from midi.models import MidiFile
from django.db import models
import os
from note_seq import midi_io



class MidiInserter:

    user = ""
    dir = "media/generated/users/"
    def __init__(self, user):
        self.user = user
        subprocess.call(['mkdir', '-p', self.dir + '/' + self.user])



    def insert(self):
        filename = subprocess.check_output(['ls', self.dir + self.user])
        filename = filename.decode('utf-8')
        filename = filename.strip()

        with open(self.dir + self.user + "/" +filename, mode="rb") as f:
            midiModel = MidiFile(midi=filename, midi_data=File(f).read(), user=self.user, source='generated', name=filename)
            midiModel.save()
            print(filename)

    def deleteFiles(self):
        subprocess.call(['rm', '-f','-r', self.dir + self.user])

    def toNoteSeq(self):
        filename = subprocess.check_output(['ls', 'media/uploaded/' + self.user])
        filename = filename.decode('utf-8')
        filename = filename.strip()

        midiFile = 'media/uploaded/' + self.user + "/" + filename

        return midi_io.midi_file_to_note_sequence(midiFile)
