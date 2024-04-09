#!/usr/bin/node
const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  charPrint (c) {
    if (!c) {
      super.print();
    } else {
      const shape = (c.repeat(this.width) + '\n').repeat(this.height).slice(0, -1);
      console.log(shape);
    }
  }
}
module.exports = Square;
