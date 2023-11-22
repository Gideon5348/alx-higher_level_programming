#!/usr/bin/node
const { list } = require('./100-data');

// Use the map function to create a new array
const newList = list.map((value, index) => value * index);

// Print both the initial list and the new list
console.log(list);
console.log(newList);
