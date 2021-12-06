#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#MelodyGenerator Class
#Gets parameters from the melody_page in view, builds and returns a subprocess call
#////////////////////////////////////////////////////////////////////////////////////////////////
class MelodyGenerator:

    steps = ""
    note = ""
    modelType = ""
    user = ""
    outDir = ""
    usersDir = "/home/david/PycharmProjects/Noodles-Interplay/interplay/media/generated/users/"

    def __init__(self, modelType, numSteps, note, user):

        self.steps = "--num_steps=" + numSteps + " "
        self.note = "--primer_melody=\"[" + note + "]\" "
        self.modelType = modelType
        #self.user = user + " "
        self.outDir = "--output_dir=" + self.usersDir + user + " "


    configDict = {
        "mono": "--config='mono' ",
        "basic": "--config='basic' ",
        "lookback": "--config='lookback' ",
        "attention": "--config='attention' ",
        "2vae": "--config='cat-mel_2bar_big' ",
        "16vae": "--config='hierdec-mel_16bar' "
    }

    #Absolute path to mag bundles
    #be sure to set them properly on the server
    modelDict = {
        "mono": "--bundle_file=/home/david/PycharmProjects/Noodles-Interplay/models/mags/mono.mag ",
        "basic": "--bundle_file=/home/david/PycharmProjects/Noodles-Interplay/models/mags/basic_rnn.mag ",
        "lookback": "--bundle_file=/home/david/PycharmProjects/Noodles-Interplay/models/mags/lookback_rnn.mag ",
        "attention": "--bundle_file=/home/david/PycharmProjects/Noodles-Interplay/models/mags/attention_rnn.mag ",
        "2vae": "--checkpoint_file=/home/david/PycharmProjects/Noodles-Interplay/models/checkpoints/cat-mel_2bar_big.tar ",
        "16vae": "--checkpoint_file=/home/david/PycharmProjects/Noodles-Interplay/models/checkpoints/hierdec-mel_16bar.tar "
    }


    outputs = "--num_outputs=1 "

    def buildCall(self):

        if self.modelType != "2vae" and self.modelType != "16vae":

            generateCall = "melody_rnn_generate "
            generateCall += self.configDict[self.modelType]
            generateCall += self.modelDict[self.modelType]
            generateCall += self.outDir
            generateCall += self.outputs
            generateCall += self.steps
            generateCall += self.note
        else:
            generateCall = "music_vae_generate "
            generateCall += self.configDict[self.modelType]
            generateCall += self.modelDict[self.modelType]
            generateCall += "--mode=sample "
            generateCall += self.outputs
            generateCall += self.outDir

        print(generateCall)
        return generateCall

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#ChordGenerator Class
#Gets parameters from the chord_page in view, builds and returns a subprocess call
#////////////////////////////////////////////////////////////////////////////////////////////////
class ChordGenerator:
    user = ""
    outDir = ""
    usersOutDir = "media/generated/users/"
    pitches = ""
    steps = ""

    def __init__(self, user, numSteps, note1, note2, note3):
        self.pitches = "--primer_pitches=\"[ "+ note1 + "," + note2 + "," + note3 + "]\" "
        self.user = user
        self.steps = "--num_steps=" + numSteps + " "
        self.outDir = "--output_dir=" + self.usersOutDir + user + " "

    bundle_file = "--bundle_file=/home/david/PycharmProjects/Noodles-Interplay/models/mags/poly_rnn.mag "
    output_num = "--num_outputs=1 "
    condtionStr = "--condition_on_primer=true --inject_primer_during_generation=false "

    def buildCall(self):
        generatedCall = "polyphony_rnn_generate "
        generatedCall += self.bundle_file
        generatedCall += self.outDir
        generatedCall += self.output_num
        generatedCall += self.steps
        generatedCall += self.pitches
        generatedCall += self.condtionStr

        return generatedCall


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#DrumGenerator Class
#Gets parameters from the drum_page in view, builds and returns a subprocess call
#///////////////////////////////////////////////////////////////////////////////////////////////
class DrumGenerator:

    user = ""
    drumType = ""
    outDir = ""
    usersOutDir = "media/generated/users/"

    def __init__(self, user, drumType):
        self.user = user
        self.drumType = drumType
        self.outDir = "--output_dir=" + self.usersOutDir + user + " "

    functionDict = {
        "basic" : "drums_rnn_generate ",
        "groove" : "music_vae_generate "
    }

    modelDict = {
        "basic" : "--config=drum_kit --bundle_file=/home/david/PycharmProjects/Noodles-Interplay/models/mags/drum_kit.mag ",
        "groove" : "--config=groovae_4bar --checkpoint_file=/home/david/PycharmProjects/Noodles-Interplay/models/checkpoints/groovae_4bar.tar --mode=sample "
    }

    outputs = "--num_outputs=1 "

    def buildCall(self):
        generateCall = self.functionDict[self.drumType]
        generateCall += self.modelDict[self.drumType]
        generateCall += self.outputs
        generateCall += self.outDir

        print(generateCall)
        return generateCall


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#Interpolater class
#Gets parameters from iterpolate_page function in views.py, builds and returns a subprocess call
#////////////////////////////////////////////////////////////////////////////////////////////////
class Interpolater:

    user = ""
    modelType = ""
    outDir = ""
    usersOutDir = "media/generated/users/"
    usersUploadDir = "media/uploaded/users/"
    file1 = ""
    file2 = ""

    def __init__(self, user, modelType, file1, file2):

        self.user = user
        self.modelType = modelType
        self.outDir = "--output_dir=" + self.usersOutDir + user + " "
        self.file1 = "--input_midi_1=" + self.usersUploadDir + file1 + " "
        self.file2 = "--input_midi_2=" + self.usersUploadDir + file2 + " "
        self.outDir = "--output_dir=" + self.usersOutDir + user + " "


    functionName = "music_vae_generate "

    modelDict = {
        "mel_2bar" : "--checkpoint_file=/home/david/PycharmProjects/Noodles-Interplay/models/checkpoints/cat-mel_2bar_big.tar ",
        "mel_16bar" : "--checkpoint_file=/home/david/PycharmProjects/Noodles-Interplay/models/checkpoints/hierdec-mel_16bar.tar ",
        "trio_16bar" : "--checkpoint_file=/home/david/PycharmProjects/Noodles-Interplay/models/checkpoints/hierdec-trio_16bar.tar "
    }

    configDict = {
        "mel_2bar": "--config='cat-mel_2bar_big' ",
        "mel_16bar": "--config='hierdec-mel_16bar' ",
        "trio_16bar": "--config='hierdec-trio_16bar' "
    }

    outputs = "--num_outputs=1 "

    def buildCall(self):
        generateCall = self.functionName
        generateCall += self.configDict[self.modelType]
        generateCall += self.modelDict[self.modelType]
        generateCall += self.outDir
        generateCall += self.file1
        generateCall += self.file2
        generateCall += self.outputs


        print(generateCall)
        return generateCall