#!/usr/bin/node

function add(a, b) {
  let c = a + b
  return c;
}
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

console.log(add(a, b));
