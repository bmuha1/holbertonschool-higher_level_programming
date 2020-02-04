#!/usr/bin/node
if (process.argv.length < 4) {
  console.log(0);
} else {
  let largest, second;
  if (process.argv[2] >= process.argv[3]) {
    largest = process.argv[2];
    second = process.argv[3];
  } else {
    largest = process.argv[3];
    second = process.argv[2];
  }

  for (let i = 4; i < process.argv.length; i++) {
    if (process.argv[i] > largest) {
      second = largest;
      largest = process.argv[i];
    }
  }
  console.log(second);
}
