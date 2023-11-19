#!/usr/bin/node
// Filename: 2-arguments.js

// Accessing command line arguments using process.argv
const args = process.argv.slice(2);

// Checking the number of arguments and printing messages accordingly
if (args.length === 0) {
  console.log('No argument');
} else if (args.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
