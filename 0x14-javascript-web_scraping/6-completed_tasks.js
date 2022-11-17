#!/usr/bin/node
// script that computes the number of tasks completed by user id.

const request = require('request');
const API = process.argv[2];

if (process.argv.length !== 3) {
  console.log('Usage: ./6-completed_tasks.js <api>');
} else {
  request(API, (err, response, body) => {
    if (err) throw err;
    const res = JSON.parse(body);

    const compl = {};
    // console.log(res.length)
    for (let i = 0; i < res.length; i++) {
      if (res[i].completed === true) {
        if (compl[res[i].userId] === undefined) {
          compl[res[i].userId] = 0;
        }
        compl[res[i].userId]++;
      }
    }
    console.log(compl);
  });
}
