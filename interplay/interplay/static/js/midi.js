console.log('midi.js called')
var dataNode = document.getElementById('midi_data');
if (dataNode) {
    console.log(dataNode.innerHTML)
    upload_string = dataNode.innerHTML
}

const midi_upload = JSON.parse(upload_string)
console.log(midi_upload)

//var noteSeq = midi_upload.sequence

const mrnn = new mm.MusicRNN('https://storage.googleapis.com/magentadata/js/checkpoints/music_rnn/basic_rnn');
console.log(mrnn);

//const noteSeq = mm.urlToNoteSequence(midi_upload);

const qNoteSeq = mm.sequences.quantizeNoteSequence(midi_upload,4)

//var noteSeq = "{" + midi_upload + "}"
console.log(qNoteSeq)

mrnn.initialize().then(() => {
    console.log("Time to continue sequence");
    mrnn.continueSequence(qNoteSeq, 6);
});