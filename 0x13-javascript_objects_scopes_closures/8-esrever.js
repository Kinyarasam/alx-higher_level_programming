#!/usr/bin/node
/**
 * esrever - returns the reversed version of a list.
 * @params list
 */
exports.esrever = function (list) {
  let counter = 0;
  const newList = [];

  while (counter < list.length - 1) {
    counter++;
  }

  while (counter >= 0) {
    newList.push(list[counter]);
    counter--;
  }

  return newList;
};
