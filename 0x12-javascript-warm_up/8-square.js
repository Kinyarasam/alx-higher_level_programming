#!/usr/bin/node
// script that prints a square
const arg = Math.floor(Number(process.argv[2]));
if (isNaN(arg)) {
  console.log('Missing size');
} else {
  loop(arg);
}

function loop (counter) {
  for (let row = 0; row < counter; row++) {
    let X = '';
    for (let col = 0; col < counter; col++) {
      X += 'X';
    }
    console.log(X);
  }
}
