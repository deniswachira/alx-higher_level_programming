#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    let counter = 0;
    const results = JSON.parse(body).results;

    for (let i = 0; i < results.length; i++) {
      const k = results[i].characters.length;
      for (let j = 0; j < k; j++) {
        if (results[i].characters[j].slice(-3) === '18/') {
          counter++;
        }
      }
    }
    console.log(counter);
  }
});
