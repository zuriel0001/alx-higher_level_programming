#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  process.argv.shift();
  process.argv.shift();
  const nums = process.argv.map(Number).sort((a, b) => a - b).reverse();
  console.log(nums[1]);
}
