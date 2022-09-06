#!/usr/bin/node
/**
 * nb0ccurences - returns the number of Occurences.
 * @params list
 * @params searchElement
 */
exports.nb0ccurences = function (list, searchElement) {
  let occurences = 0;
  let counter = 0;

  while (counter < list.length) {
    if (searchElement === list[counter]) {
      occurences += 1;
    }

    counter++;
  }

  return occurences;
};
