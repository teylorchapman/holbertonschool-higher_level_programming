#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length < 2) {
  console.log(0);
} else {
  let first = parseInt(args[0]);
  let second = parseInt(args[1]);

  if (second > first) {
    [first, second] = [second, first];
  }

  for (let i = 2; i < args.length; i++) {
    const numba = parseInt(args[i]);
    if (numba > first) {
      second = first;
      first = numba;
    } else if (numba > second) {
      second = numba;
    }
  }

  console.log(second);
}
