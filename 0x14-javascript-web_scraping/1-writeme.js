#!/usr/bin/node
// Script that writes a string to a file

const fs = require('fs');
const FILE_NAME = process.argv[2];
const TEXT = process.argv[3];

fs.writeFile(FILE_NAME, TEXT, (error) => {
  if (error) throw error;
});
