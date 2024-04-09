#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const shape = ('X'.repeat(this.width) + '\n').repeat(this.height).slice(0, -1);
    console.log(shape);
  }
}
module.exports = Rectangle;
