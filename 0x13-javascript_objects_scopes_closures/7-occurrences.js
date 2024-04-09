#!/usr/bin/node
exports.nbOccurences = function (list, query) {
  let occurence = 0;
  list.forEach(element => {
    if (element === query) {
      occurence++;
    }
  });
  return occurence;
};
