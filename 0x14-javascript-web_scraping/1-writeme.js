#!/usr/bin/node

const fs = require('fs');

<<<<<<< HEAD
const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(content);
});

=======
fs.writeFile(process.argv[2], process.argv[3], 'utf-8',
  function (err) {
    if (err) {
      console.log(err);
    }
  });
>>>>>>> 3faa8cd32babf6a8148bef6d7582da1c0ea5e707
