#!/usr/bin/node
// script that reads and prints the content of a file.

const fs = require('fs');
const FILE_PATH = process.argv[2];

fs.readFile(FILE_PATH, 'utf-8', (error, data) => {
  console.log(data || error);
});
