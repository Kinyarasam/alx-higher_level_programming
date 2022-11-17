#!/usr/bin/node
// Script that prints all characters of a Star Wars movie:

const request = require('request');
const STAR_WARS_API = 'https://swapi-api.hbtn.io/api/films/';
const url = `${STAR_WARS_API}` + process.argv[2];

if (process.argv.length !== 3) {
  console.log('Usage: ./100-starwars_characters.js <Movie_id>');
} else {
  request(url, (err, response, body) => {
    if (err) throw err;

    const data = JSON.parse(body);
    const res = data.characters;

    for (let i = 0; i < res.length; i++) {
      request(res[i], (err, response, body) => {
        if (err) throw err;

        console.log(JSON.parse(body).name);
      });
    }
  });
}
