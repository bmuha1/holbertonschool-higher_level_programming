#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) throw error;
  let count = 0;
  for (const film of JSON.parse(body).results) {
    if (film.characters.includes('https://swapi.co/api/people/18/')) {
      count++;
    }
  }
  console.log(count);
});
