#!/usr/bin/node
// script that computes and prints a factorial
const count = Number(process.argv[2]);

function factorial (value) {
  if (isNaN(value) || value === 0) {
    return (1);
  } else {
    return (value * factorial(value - 1));
  }
  // return (isNaN(value) || value === 0 ? 1 : value * factorial(value - 1));
}

console.log(factorial(count));
