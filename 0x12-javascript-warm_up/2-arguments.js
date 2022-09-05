#!/usr/bin/node

// Script that prints a message depending of the number of arguments passed:
let result;
(process.argv.length < 3 ? result = 'No arguement' : process.argv.length === 3 ? result = 'Argument found' : result = 'Arguements found');
console.log(result);
