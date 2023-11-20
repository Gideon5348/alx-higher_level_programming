#!/usr/bin/node
// Filename: 102-add_me_maybe.js

exports.addMeMaybe = function (number, theFunction) {
  theFunction(number + 1);
};
