#!/usr/bin/node
// script that prints the addition of 2 integers
const num1 = process.argv[2];
const num2 = process.argv[3];

add(num1, num2);

function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}
