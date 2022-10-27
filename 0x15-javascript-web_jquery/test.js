#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json'
request(url, (data, response, error) =>{
	if (error) throw error;
	console.log(data);
});
