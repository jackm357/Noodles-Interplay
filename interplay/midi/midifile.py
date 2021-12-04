import subprocess
from django.core.files.base import ContentFile, File
from midi.models import MidiFile
from django.db import models
import os
from note_seq import midi_io
from note_seq import sequences_lib



class MidiInserter:

    user = ""
    gDir = "media/generated/users/"
    uDir = "media/uploaded/"
    def __init__(self, user):
        self.user = user
        subprocess.call(['mkdir', '-p', self.gDir + '/' + self.user])



    def insert(self, type):
        filename = subprocess.check_output(['ls', self.gDir + self.user])
        filename = filename.decode('utf-8')
        filename = filename.strip()

        with open(self.gDir + self.user + "/" +filename, mode="rb") as f:
            midiModel = MidiFile(midi=filename, midi_data=File(f).read(), user=self.user, source='generated-'+type, name=filename)
            midiModel.save()
            print(filename)

    def deleteFiles(self):
        subprocess.call(['rm', '-f', '-r', self.gDir + self.user])
        subprocess.call(['rm', '-f', '-r', self.uDir + self.user])

    def toNoteSeq(self):
        filename = subprocess.check_output(['ls', 'media/uploaded/' + self.user])
        filename = filename.decode('utf-8')
        filename = filename.strip()

        midiFile = 'media/uploaded/' + self.user + "/" + filename
        noteSeq = midi_io.midi_file_to_note_sequence(midiFile)
        qSeq = sequences_lib.quantize_note_sequence(noteSeq, 4)
        #midi_io.note_sequence_to_midi_file(qSeq, midiFile, drop_events_n_seconds_after_last_note=None)

        return qSeq