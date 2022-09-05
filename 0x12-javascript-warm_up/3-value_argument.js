#!/usr/bin/node
// Script that prints the first argument passed to it:

(process.argv[2] ? console.log(process.argv[2]) : console.log('No arguement'));
