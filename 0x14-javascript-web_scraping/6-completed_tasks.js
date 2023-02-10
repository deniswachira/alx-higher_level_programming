#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const output = {};
    const content = JSON.parse(body);

    for (let i = 1; i < 11; i++) {
      let counter = 0;
      for (let j = 0; j < content.length; j++) {
        if (content[j].userId === i && content[j].completed === true) {
          counter++;
        }
      }
      if (counter > 0) {
        output[i] = counter;
      }
    }
    console.log(output);
  }
});
