#!/usr/bin/node
// Script that prints all characters of a Star Wars movie

const request = require('request');
const STAR_WARS_API = 'https://swapi-api.hbtn.io/api/films/';
const MOVIE_ID = process.argv[2];

if (process.argv.length !== 3) {
  console.log('Usage: ./101-starwars_characters.js <Movie_ID>');
} else {
  function getHelpReq (list, count) {
    if (count === list.length) return;

    request(list[count], (err, response, body) => {
      if (err) throw err;

      console.log(JSON.parse(body).name);
      getHelpReq(list, count + 1);
    });
  }

  request(`${STAR_WARS_API}` + MOVIE_ID, (err, response, body) => {
    if (err) throw err;

    const res = JSON.parse(body).characters;

    getHelpReq(res, 0);
  });
}
