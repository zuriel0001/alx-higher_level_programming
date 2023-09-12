#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  process.argv.shift();
  process.argv.shift();
  const Myarray = process.argv.map(Number).sort((a, b) => a - b).reverse();
  console.log(Myarray[1]);
}
