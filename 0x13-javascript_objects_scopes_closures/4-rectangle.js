#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (parseInt(w) > 0 && parseInt(h) > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

Rectangle.prototype.print = function () {
  for (let i = 0; i < this.height; i++) {
    console.log('X'.repeat(this.width));
  }
};

Rectangle.prototype.rotate = function () {
  [this.width, this.height] = [this.height, this.width];
};

Rectangle.prototype.double = function () {
  this.width *= 2;
  this.height *= 2;
};

module.exports = Rectangle;
