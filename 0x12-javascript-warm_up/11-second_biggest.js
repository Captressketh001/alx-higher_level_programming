#!/usr/bin/node

const arg = process.argv;
function compare (a, b) {
  return b - a;
}

if (arg.length === 2) {
  console.log(0);
} else if (arg.length === 3) {
  console.log(0);
} else {
  const index = arg.slice(2);
  const value = index.sort(compare).reverse();
  console.log(value[1]);
}
