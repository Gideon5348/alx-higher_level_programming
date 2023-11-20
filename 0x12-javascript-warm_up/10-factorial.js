#!/usr/bin/node
// Filename: 10-factorial.js

// Define the recursive factorial function
function factorial (n) {
  if (isNaN(n) || n < 0) {
    return 1; // Factorial of NaN or negative number is 1
  }
  if (n === 0 || n === 1) {
    return 1; // Factorial of 0 or 1 is 1
  } else {
    return n * factorial(n - 1); // Recursive call for factorial
  }
}

// Accessing the second element of process.argv (the first argument)
const arg = parseInt(process.argv[2], 10);

// Compute and print the factorial
const result = factorial(arg);
console.log(result);
