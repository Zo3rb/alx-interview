#!/usr/bin/node
/**
 * prints all characters of a Star Wars movie
 * */

const request = require('request');

const movieNum = process.argv[2];
const API_URL = `https://swapi-api.alx-tools.com/api/films/${movieNum}`;

(async function getMovieCharacters() {
  request(API_URL, (error, response, body) => {
    if (!error) {
      const data = JSON.parse(body).characters;
      data.forEach((charLink) => {
        request(charLink, (err, res, bod) => {
          if (!err) {
            console.log(JSON.parse(bod).name);
          }
        });
      });
    }
  });
}());

