#!/usr/bin/node
// Filename: 7-multi_c.js

// Accessing the second element of process.argv (the first argument)
const arg = process.argv[2];

// Attempting to convert the argument to an integer
const occurrences = parseInt(arg, 10);

// Checking if the conversion was successful and printing the output
if (isNaN(occurrences)) {
  console.log('Missing number of occurrences');
} else {
  // Using a loop to print "C is fun" x times
  const numOccurrences = Math.abs(occurrences);
  const message = 'C is fun';

  for (let i = 0; i < numOccurrences; i++) {
    console.log(message);
  }
}
