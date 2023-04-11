#!/usr/bin/node
const numba = parseInt(process.argv[2]);

function factorial (numba) {
  if (isNaN(numba)) {
    return 1;
  } else if (numba === 0) {
    return 1;
  } else {
    return numba * factorial(numba - 1);
  }
}

console.log(factorial(numba));
