#!/usr/bin/node
// Filename: 5-to_integer.js

// Accessing the second element of process.argv (the first argument)
const arg = process.argv[2];

// Attempting to convert the argument to an integer
const number = parseInt(arg, 10);

// Checking if the conversion was successful and printing the result
if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${number}`);
}
