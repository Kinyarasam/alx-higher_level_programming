#!/usr/bin/node
// script that prints x times “C is fun”
if (process.argv.length < 3) {
  console.log('Missing number of occurrences');
} else {
  const counter = parseInt(process.argv[2]);
  loop(counter);
}

function loop (counter) {
  while (counter > 0) {
    console.log('C is fun');
    counter--;
  }
}
