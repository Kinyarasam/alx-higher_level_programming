#!/usr/bin/node

// Script that prints a message depending of the number of arguments passed:
(process.argv.length < 3 ? console.log('No arguement') : process.argv.length === 3 ? console.log('Argument found') : console.log('Arguements found'));
