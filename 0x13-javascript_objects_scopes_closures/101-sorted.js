#!/usr/bin/node
const dict = require('./101-data').dict;
const sorted = (obj) => {
  const reversed = {};
  Object.keys(obj).forEach((key) => {
    reversed[obj[key]] = reversed[obj[key]] || [];
    reversed[obj[key]].push(key);
  });
  return reversed;
};
console.log(sorted(dict));
