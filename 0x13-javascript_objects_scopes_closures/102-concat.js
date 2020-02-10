#!/usr/bin/node
// console.log(process.argv[2] + process.argv[3]);
const fs = require('fs');
for (let i = 2; i <= 3; i++) {
  fs.readFile(process.argv[i], 'utf8', function (err, data) {
    if (err) throw err;
    fs.appendFile(process.argv[4], data, (err) => {
      if (err) throw err;
    });
  });
}
