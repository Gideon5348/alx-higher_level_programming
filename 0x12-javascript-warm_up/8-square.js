#!/usr/bin/node
// Filename: 8-square.js

// Accessing the second element of process.argv (the first argument)
const arg = process.argv[2];

// Attempting to convert the argument to an integer
const size = parseInt(arg, 10);

// Checking if the conversion was successful and printing the square
if (isNaN(size) || size <= 0) {
  console.log('Missing size');
} else {
  // Using nested loops to print the square
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
