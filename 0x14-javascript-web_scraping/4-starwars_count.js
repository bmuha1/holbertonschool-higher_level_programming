#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) throw error;
  let count = 0;
  for (let i = 0; i < JSON.parse(body).count; i++) {
    if (JSON.parse(body).results[i].characters.includes(
      'https://swapi.co/api/people/18/')) {
      count++;
    }
  }
  console.log(count);
});
