// Welcome and Menu Module
const { getValidMenuChoice } = require('./inputValidation');

const LINE = '='.repeat(30);

function showWelcome() {
  console.log(LINE);
  console.log(' INTERACTIVE QUIZ & LEARNING APP');
  console.log(LINE);
  console.log('Welcome! Answer each question by typing the option number.\n');
  console.log('Rules:');
  console.log('1. You will see one question at a time.');
  console.log('2. Type the number of your chosen option.');
  console.log('3. Invalid answers will be asked again.\n');
}

function showMenu() {
  console.log('1. Start Quiz');
  console.log('2. Exit');
}

// Shows the menu and returns "start" or "exit".
function handleMenu() {
  showMenu();
  const choice = getValidMenuChoice();
  switch (choice) {
    case 1:
      return 'start';
    case 2:
      return 'exit';
    default:
      return 'exit';
  }
}

module.exports = { showWelcome, showMenu, handleMenu, LINE };
