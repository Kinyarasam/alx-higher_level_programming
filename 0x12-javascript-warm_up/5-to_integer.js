#!/usr/bin/node
// script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer:
const arg = Math.floor(Number(process.argv[2]));
console.log(isNaN(arg) ? 'Not a number' : `My number: ${arg}`);
