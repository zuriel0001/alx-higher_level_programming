#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  let x = 0;
  while ((len - x) > 0) {
    const tmp = list[len];
    list[len] = list[x];
    list[x] = tmp;
    x++;
    len--;
  }
  return list;
