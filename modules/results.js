// Results Module
const { calculatePercentage, getPerformanceMessage } = require('./score');
const { LINE } = require('./menu');

function displayResults(score, totalQuestions) {
  const percentage = calculatePercentage(score.correct, totalQuestions);
  console.log(`\n${LINE}`);
  console.log(' 🏆 QUIZ RESULTS 🏆');
  console.log(LINE);
  console.log(`Total Questions:   ${totalQuestions}`);
  console.log(`Correct Answers:   ${score.correct}`);
  console.log(`Incorrect Answers: ${score.incorrect}`);
  console.log(`Score:             ${score.correct} / ${totalQuestions}`);
  console.log(`Percentage:        ${percentage}%`);
  console.log(`\n${getPerformanceMessage(percentage)}\n`);
  return percentage;
}

module.exports = { displayResults };
