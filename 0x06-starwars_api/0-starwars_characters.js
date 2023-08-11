#!/usr/bin/node

const request = require('request');
<<<<<<< HEAD
=======

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
>>>>>>> 841aadbc490c6b332b563a1cbc7d75ba75552c86

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, res, body) {
  if (err) throw err;
  const actors = JSON.parse(body).characters;
  exactOrder(actors, 0);
});
const exactOrder = (actors, x) => {
  if (x === actors.length) return;
  request(actors[x], function (err, res, body) {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    exactOrder(actors, x + 1);
  });
};
