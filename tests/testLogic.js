// Manual tests for pure logic.  Run with:  node tests/testLogic.js
const { parseOptionNumber } = require('../modules/inputValidation');
const { calculatePercentage, getPerformanceMessage, createScore, recordAnswer } = require('../modules/score');
const { checkAnswer } = require('../modules/quiz');
const { isValidQuestion } = require('../modules/questionData');

let passed = 0;
let failed = 0;
function expect(name, actual, expected) {
  const ok = actual === expected;
  ok ? passed++ : failed++;
  console.log(`${ok ? 'PASS' : 'FAIL'} - ${name} (got ${JSON.stringify(actual)}, expected ${JSON.stringify(expected)})`);
}

expect('valid "3"', parseOptionNumber('3', 4), 3);
expect('padded " 3 "', parseOptionNumber(' 3 ', 4), 3);
expect('zero', parseOptionNumber('0', 4), null);
expect('above range', parseOptionNumber('5', 4), null);
expect('empty', parseOptionNumber('', 4), null);
expect('decimal', parseOptionNumber('2.5', 4), null);
expect('negative', parseOptionNumber('-1', 4), null);
expect('letters', parseOptionNumber('abc', 4), null);
expect('two-option question', parseOptionNumber('2', 2), 2);

expect('5/5 = 100%', calculatePercentage(5, 5), 100);
expect('0/5 = 0%', calculatePercentage(0, 5), 0);
expect('3/5 = 60%', calculatePercentage(3, 5), 60);
expect('2/3 = 67%', calculatePercentage(2, 3), 67);
expect('empty list = 0% (no NaN)', calculatePercentage(0, 0), 0);
expect('100% message', getPerformanceMessage(100).startsWith('Excellent'), true);
expect('0% message', getPerformanceMessage(0).startsWith('Keep practicing'), true);

const q = { question: 'Q', options: ['a', 'b', 'c'], correctAnswer: 1 };
expect('checkAnswer right', checkAnswer(q, 2), true);
expect('checkAnswer wrong', checkAnswer(q, 3), false);
expect('isValidQuestion ok', isValidQuestion(q), true);
expect('isValidQuestion bad index', isValidQuestion({ ...q, correctAnswer: 9 }), false);

const s = createScore();
recordAnswer(s, true);
recordAnswer(s, false);
expect('score correct', s.correct, 1);
expect('score incorrect', s.incorrect, 1);

console.log(`\n${passed} passed, ${failed} failed`);
process.exitCode = failed === 0 ? 0 : 1;
