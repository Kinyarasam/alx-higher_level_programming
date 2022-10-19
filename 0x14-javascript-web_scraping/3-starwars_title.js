#!/usr/bin/node
// Prints the title of a Star Wars movie where the episode number matched a given integer.

const request = require('request');
const STAR_WARS_API = 'https://swapi-api.hbtn.io/api/films/';
const MOVIE_ID = process.argv[2];

request(STAR_WARS_API + MOVIE_ID, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
