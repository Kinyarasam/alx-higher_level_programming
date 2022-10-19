#!/usr/bin/node
// Script that display the status code of a GET request.

const request = require('request');
const URL_LINK = process.argv[2];

request(URL_LINK, (error, response, data) => {
  console.log('code:', response.statusCode); // Print the response status code if a response was received
  if (error) throw error;
});
