#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch movie data. Status code:', response.statusCode);
    return;
  }

  const movieData = JSON.parse(body);
  const characterUrls = movieData.characters;

  // Function to fetch character name for a given URL
  const fetchCharacterName = (url) => {
    return new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          reject(error);
          return;
        }
        if (response.statusCode !== 200) {
          reject(`Failed to fetch character data. Status code: ${response.statusCode}`);
          return;
        }
        const characterData = JSON.parse(body);
        resolve(characterData.name);
      });
    });
  };

  // Array to store promises for fetching character names
  const characterPromises = characterUrls.map(url => fetchCharacterName(url));

  // Wait for all promises to resolve
  Promise.all(characterPromises)
    .then(characterNames => {
      // Print character names
      characterNames.forEach(name => console.log(name));
    })
    .catch(error => {
      console.error('Error:', error);
    });
});
