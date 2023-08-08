#!/usr/bin/node
/**
 * prints all characters of a Star Wars movie
 * */

const request = require('request');
const movieNum = process.argv[2];
const API_URL = `https://swapi-api.alx-tools.com/api/films/${movieNum}`;

(async function getMovieCharacters(movieNum) {
    request(API_URL, (error, response, body) => {
        if (!error) {
            let data = JSON.parse(body);
            for (let charLink of data.characters) {
                request(charLink, (error, response, body) => {
                    if (!error) {
                        body = JSON.parse(body);
                        console.log(body.name);
                    }
                })
            }
        }
    })
})();

