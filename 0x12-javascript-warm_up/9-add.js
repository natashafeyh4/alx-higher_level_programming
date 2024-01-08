#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const firstNumber = parseInt(process.argv[2], 10);
const secondNumber = parseInt(process.argv[3], 10);

if (Number.isNaN(firstNumber) || Number.isNaN(secondNumber)) {
  console.log('NaN');
} else {
  console.log(add(firstNumber, secondNumber));
}
