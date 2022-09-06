#!/usr/bin/node
// Script that prints the first argument passed to it:
let output;

(process.argv[2] ? output = process.argv[2] : output = 'No argument');
console.log(output);
