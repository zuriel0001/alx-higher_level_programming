#!/usr/bin/node
const MyObject = {
  type: 'object',
  value: 12
};
console.log(MyObject);
MyObject.incr = function () {
  this.value++;
};
MyObject.incr();
console.log(MyObject);
MyObject.incr();
console.log(MyObject);
MyObject.incr();
console.log(MyObject);
