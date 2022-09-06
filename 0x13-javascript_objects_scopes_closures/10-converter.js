#!/usr/bin/node
/**
 * converter - converts a number from base 10 to another base.
 * @params base
 */
exports.converter = function (base) {
  return num => num.toString(base);
};
