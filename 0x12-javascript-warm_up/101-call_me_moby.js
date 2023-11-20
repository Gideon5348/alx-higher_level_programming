#!/usr/bin/node
// Filename: 101-call_me_moby.js

exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
