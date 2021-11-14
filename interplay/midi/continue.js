const args = process.argv.slice(2)
const file1 = args[0]
const file2 = args[1]
var both = file1 + ' ' + file2

var fs = require('fs')
var input = "../media/uploaded/hogleg14/Jack-js-test.txt"

fs.readFile(input, 'utf-8', function(err, data){
    if(err) throw err;
    
    fs.writeFile(input, both, 'utf-8', function(err, data){
        if (err) throw err;
    })
})