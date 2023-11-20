#!/usr/bin/node
// Filename: 11-second_biggest.js

// Accessing the list of arguments (starting from index 2)
const args = process.argv.slice(2);

// Checking if no argument or only one argument is passed
if (args.length <= 1) {
  console.log(0);
} else {
  // Converting arguments to integers and sorting them in descending order
  const sortedIntegers = args.map(arg => parseInt(arg, 10)).sort((a, b) => b - a);

  // Printing the second biggest integer
  console.log(sortedIntegers[1]);
}
