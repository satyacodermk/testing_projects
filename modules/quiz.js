// Quiz Execution Module
const { getValidAnswer, waitForEnter } = require('./inputValidation');
const { createScore, recordAnswer } = require('./score');

function displayQuestion(question, index, total) {
  console.log(`\nQuestion ${index + 1} of ${total}`);
  console.log(question.question);
  for (let i = 0; i < question.options.length; i++) {
    console.log(`${i + 1}. ${question.options[i]}`);
  }
}

// userChoice is 1-based (what the user typed); correctAnswer is 0-based.
function checkAnswer(question, userChoice) {
  return userChoice - 1 === question.correctAnswer;
}

function showFeedback(question, isCorrect, score, answeredCount) {
  console.log('');
  if (isCorrect) {
    console.log('✅ Correct! Well done!');
  } else {
    const right = question.correctAnswer;
    console.log('❌ Incorrect.');
    console.log(`The correct answer was: ${right + 1}. ${question.options[right]}`);
  }
  console.log(`Current score: ${score.correct} / ${answeredCount}`);
}

// Runs every question in order and returns a fresh score object.
function runQuiz(questions) {
  const score = createScore(); // reset on every round
  for (let i = 0; i < questions.length; i++) {
    const question = questions[i];
    displayQuestion(question, i, questions.length);
    const userChoice = getValidAnswer(question.options.length);
    const isCorrect = checkAnswer(question, userChoice);
    recordAnswer(score, isCorrect);
    showFeedback(question, isCorrect, score, i + 1);
    if (i < questions.length - 1) {
      waitForEnter();
    }
  }
  return score;
}

module.exports = { displayQuestion, checkAnswer, showFeedback, runQuiz };
