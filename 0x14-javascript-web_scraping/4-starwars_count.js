#!/usr/bin/node
// Script that prints the number of movies where the character "Wedge Antilles" is present.

const req = require('request');
const STAR_WARS_API = process.argv[2];
const CHARACTER_ID = '18';

req(STAR_WARS_API, (error, response, body) => {
  let NO_OF_MOVIES = 0;

  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const results = JSON.parse(body).results;
    for (let i = 0; i < results.length; i++) {
      const characters = results[i].characters;
      for (let x = 0; x < characters.length; x++) {
        (characters[x].search(CHARACTER_ID) > 0) ? NO_OF_MOVIES++ : NO_OF_MOVIES;
      }
    }
  }
  console.log(NO_OF_MOVIES);
});
