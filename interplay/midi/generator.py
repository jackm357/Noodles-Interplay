from django.http import HttpResponse

class Generator:

    steps = ""
    note = ""
    modelType = ""

    def __init__(self, modelType, numSteps, note):
        #self.request = request
        # modelType = request.get('model')
        # numSteps = request.get('steps')
        # note = request.get('note')

        self.steps = "--num_steps=" + numSteps + " "
        self.note = "--primer_melody=\"[" + note + "]\" "
        self.modelType = modelType

        #call = buildCall()



    functionName = "melody_rnn_generate "

    configDict = {
        "mono": "--config='mono' ",
        "basic": "--config='basic' ",
        "lookback": "--config='lookback' ",
        "attention": "--config='attention' "
    }

    modelDict = {
        "mono": "--bundle_file=/home/david/PycharmProjects/Noodles-Interplay/interplay/midi/mono.mag ",
        "basic": "--bundle_file=/home/david/PycharmProjects/Noodles-Interplay/mags/basic_rnn.mag ",
        "lookback": "--bundle_file=/home/david/PycharmProjects/Noodles-Interplay/mags/lookback_rnn.mag ",
        "attention": "--bundle_file=/home/david/PycharmProjects/Noodles-Interplay/mags/attention_rnn.mag "
    }

    outDir = "--output_dir=/tmp/melody_rnn/generated "
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
