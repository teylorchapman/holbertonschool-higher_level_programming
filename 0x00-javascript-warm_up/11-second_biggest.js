#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length < 2) {
  console.log(0);
} else {
  let one = parseInt(args[0]);
  let two = parseInt(args[1]);

  if (two > one) {
    [one, two] = [two, one];
  }

  for (let i = 2; i < args.length; i++) {
    const numba = parseInt(args[i]);
    if (numba > one) {
      two = one;
      one = numba;
    } else if (numba > two) {
      two = numba;
    }
  }

  console.log(two);
}
