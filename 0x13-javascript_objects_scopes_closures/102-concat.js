#!/usr/bin/node
const fs = require('fs');
const file0 = fs.readFileSync(process.argv[2]).toString();
const file1 = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], file0 + file1);
