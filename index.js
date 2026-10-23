// Entry point: ties every module together.  Run with:  node index.js
// Optional flag: node index.js --shuffle   (random question order)
const { loadQuestions, shuffleQuestions } = require('./modules/questionData');
const { showWelcome, handleMenu } = require('./modules/menu');
const { runQuiz } = require('./modules/quiz');
const { displayResults } = require('./modules/results');
const { askPlayAgain, sayGoodbye } = require('./modules/restart');

function main() {
  try {
    let questions = loadQuestions();
    if (process.argv.includes('--shuffle')) {
      questions = shuffleQuestions(questions);
    }

    showWelcome();

    let running = true;
    while (running) {
      const action = handleMenu();

      if (action === 'exit') {
        sayGoodbye();
        running = false;
        continue;
      }

      if (questions.length === 0) {
        console.log('\nNo questions available. Add some to input/questions.json.\n');
        continue;
      }

      let playing = true;
      while (playing) {
        const score = runQuiz(questions);
        displayResults(score, questions.length);
        playing = askPlayAgain();
      }
      sayGoodbye();
      running = false;
    }
  } catch (error) {
    if (error.message === 'INPUT_CLOSED') {
      console.log('\n\nInput closed. Goodbye!');
    } else {
      console.log(`\nUnexpected error: ${error.message}`);
      process.exitCode = 1;
    }
  }
}

main();
