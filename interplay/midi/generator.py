from django.http import HttpResponse

class MelodyGenerator:

    steps = ""
    note = ""
    modelType = ""
    user = ""
    outDir = ""
    usersDir = "/home/david/PycharmProjects/Noodles-Interplay/interplay/media/generated/melody/users/"

    def __init__(self, modelType, numSteps, note, user):

        self.steps = "--num_steps=" + numSteps + " "
        self.note = "--primer_melody=\"[" + note + "]\" "
        self.modelType = modelType
        self.user = user + " "
        self.outDir = "--output_dir=" + self.usersDir + self.user

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
        "mono": "--bundle_file=/home/david/PycharmProjects/Noodles-Interplay/interplay/midi/mono.mag ",
        "basic": "--bundle_file=/home/david/PycharmProjects/Noodles-Interplay/mags/basic_rnn.mag ",
        "lookback": "--bundle_file=/home/david/PycharmProjects/Noodles-Interplay/mags/lookback_rnn.mag ",
        "attention": "--bundle_file=/home/david/PycharmProjects/Noodles-Interplay/mags/attention_rnn.mag "
    }

    #directory to output the midi file to
    #will need to figure out a way to put it in the database for the user

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