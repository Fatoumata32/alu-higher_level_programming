#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFileSync(filePath, body, 'utf-8');
    if (error) {
      console.log(error);
    }
  }
});
