#!/usr/bin/node
const request = require('request');

const APIurl = process.argv[2];
const characterid = 18;

request(`${APIurl}?format=json`, (err, resp, body) => {
    if (err) {
      console.error(err);
      return;
    }
  
    if (resp.statusCode !== 200) {
      console.error(`Unexpected status code: ${resp.statusCode}`);
      return;
    }
  
    const movies = JSON.parse(body).results;
    const wedgiemovies = movies.filter(movie =>
      movie.characters.some(characterurl => characterurl.includes(`/${characterid}/`))
    );
  
    console.log(`${wedgiemovies.length}`);
  });
