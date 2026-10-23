// Restart and Exit Module
const { getYesNo } = require('./inputValidation');

function askPlayAgain() {
  return getYesNo('Play again? (y/n): ');
}

function sayGoodbye() {
  console.log('Thanks for playing. Goodbye!');
}

module.exports = { askPlayAgain, sayGoodbye };
