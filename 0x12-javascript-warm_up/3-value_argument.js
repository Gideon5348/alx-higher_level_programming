#!/usr/bin/node
// Filename: 3-value_argument.js

// Accessing the second element of process.argv (the first argument)
const argument = process.argv[2];

// Checking if an argument is present and printing accordingly
if (!argument) {
  console.log('No argument');
} else {
  console.log(argument);
}
