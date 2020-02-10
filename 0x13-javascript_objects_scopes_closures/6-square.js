#!/usr/bin/node
const Square = require('./5-square');

Square.prototype.charPrint = function (c) {
  if (!c) {
    c = 'X';
  }
  for (let i = 0; i < this.width; i++) {
    console.log(c.repeat(this.width));
  }
};

module.exports = Square;
