#!/usr/bin/node
// JS Script script that writes a string to a file
let fs = require('fs');
let argstr = process.argv[3];
fs.writeFile(process.argv[2], argstr, function (err, argstr) {
  if (err) {
    console.log(err);
  }
});
