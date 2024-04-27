#!/usr/bin/node
const num = Number(process.argv[2]);
if (isNaN(num)) {
  console.log('Missing numberr of occurences');
} else {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
