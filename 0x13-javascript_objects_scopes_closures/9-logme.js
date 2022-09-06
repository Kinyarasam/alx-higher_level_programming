#!/usr/bin/node
let index = 0;

/**
 * logMe - prints the number of arguments already printef and the new argument value
 * @params item
 */
exports.logMe = function (item) {
  console.log(`${index++}: ${item}`);
}
