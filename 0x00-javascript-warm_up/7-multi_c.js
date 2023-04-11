#!/usr/bin/node
const numba = parseInt(process.argv[2]);

if (!isNaN(numba)) {
  for (let i = 0; i < numba; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
