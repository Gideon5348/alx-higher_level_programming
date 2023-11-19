#!/usr/bin/node
// Filename: 4-concat.js

// Accessing the second and third elements of process.argv
const arg1 = process.argv[2] || 'undefined';
const arg2 = process.argv[3] || 'undefined';

// Printing the formatted output
console.log(`${arg1} is ${arg2}`);
