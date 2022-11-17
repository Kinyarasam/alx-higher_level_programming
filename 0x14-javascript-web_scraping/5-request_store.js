#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file.

const request = require('request');
const fs = require('fs');
const REQ_API = process.argv[2];
const FILENAME = process.argv[3];

if (process.argv.length !== 4) {
  console.log('Usage: ./5-request_store.js <api> <filename>');
} else {
  request(`${REQ_API}`, (error, response, body) => {
    const data = response.body;

    fs.writeFile(FILENAME, data, (err) => {
      if (err) throw err;
    });

    if (error) throw error;
  });
}
