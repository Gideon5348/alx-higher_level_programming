#!/usr/bin/node
// Filename: 9-add.js

// Define the add function
function add (a, b) {
  return a + b;
}

// Accessing the second and third elements of process.argv
const arg1 = parseInt(process.argv[2], 10);
const arg2 = parseInt(process.argv[3], 10);

// Checking if the conversion was successful and printing the result
if (isNaN(arg1) || isNaN(arg2)) {
  console.log('NaN');
} else {
  const result = add(arg1, arg2);
  console.log(result);
}
