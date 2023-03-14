#!/usr/bin/node
let index = process.argv[2]
if (index === undefined) {
  console.log('No argument');
}else {
  console.log(index);
}
