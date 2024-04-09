#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length;
  const revList = [];
  list.forEach(element => {
    revList[--len] = element;
  });
  return revList;
};
