from django.http import HttpResponse

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

    functionName = "melody_rnn_generate "

    configDict = {
        "mono": "--config='mono' ",
        "basic": "--config='basic' ",
        "lookback": "--config='lookback' ",
        "attention": "--config='attention' "
    }

    #Absolute path to mag bundles
    #be sure to set them properly on the server
    modelDict = {
        "mono": "--bundle_file=/home/david/PycharmProjects/Noodles-Interplay/models/mags/mono.mag ",
        "basic": "--bundle_file=/home/david/PycharmProjects/Noodles-Interplay/models/mags/basic_rnn.mag ",
        "lookback": "--bundle_file=/home/david/PycharmProjects/Noodles-Interplay/models/mags/lookback_rnn.mag ",
        "attention": "--bundle_file=/home/david/PycharmProjects/Noodles-Interplay/models/mags/attention_rnn.mag "
    }


    outputs = "--num_outputs=1 "

    def buildCall(self):

        generateCall = self.functionName
        generateCall += self.configDict[self.modelType]
        generateCall += self.modelDict[self.modelType]
        generateCall += self.outDir
        generateCall += self.outputs
        generateCall += self.steps
        generateCall += self.note

        print(generateCall)
        return generateCall

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