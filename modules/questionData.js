// Question Data Module: loads, validates and (optionally) shuffles questions.
// correctAnswer is the ZERO-BASED index of the right option (0 = first option).
const fs = require('fs');
const path = require('path');

const QUESTIONS_FILE = path.join(__dirname, '..', 'input', 'questions.json');

// Built-in fallback used when input/questions.json is missing or invalid.
const defaultQuestions = [
  {
    question: 'What keyword declares a constant in JavaScript?',
    options: ['var', 'let', 'const', 'static'],
    correctAnswer: 2,
  },
  {
    question: 'Which loop is best when you know how many times to repeat?',
    options: ['for', 'while', 'do...while', 'switch'],
    correctAnswer: 0,
  },
  {
    question: 'Which method converts an object into a JSON string?',
    options: ['JSON.parse()', 'JSON.stringify()', 'JSON.convert()', 'Object.toJSON()'],
    correctAnswer: 1,
  },
];

// Returns true only if the object has the expected question shape.
function isValidQuestion(q) {
  return (
    q !== null &&
    typeof q === 'object' &&
    typeof q.question === 'string' &&
    q.question.trim() !== '' &&
    Array.isArray(q.options) &&
    q.options.length >= 2 &&
    q.options.every((opt) => typeof opt === 'string') &&
    Number.isInteger(q.correctAnswer) &&
    q.correctAnswer >= 0 &&
    q.correctAnswer < q.options.length
  );
}

// Reads questions with JSON.parse; falls back to defaults on any problem.
function loadQuestions(filePath = QUESTIONS_FILE) {
  try {
    const raw = fs.readFileSync(filePath, 'utf8');
    const parsed = JSON.parse(raw);
    if (!Array.isArray(parsed)) {
      throw new Error('questions.json must contain an array');
    }
    const valid = parsed.filter(isValidQuestion);
    if (valid.length !== parsed.length) {
      console.log(`Note: skipped ${parsed.length - valid.length} invalid question(s) in questions.json.`);
    }
    return valid;
  } catch (error) {
    console.log(`Could not load questions file (${error.message}). Using built-in questions.`);
    return [...defaultQuestions];
  }
}

// Saves questions with JSON.stringify (optional helper for extending the app).
function saveQuestions(questions, filePath = QUESTIONS_FILE) {
  try {
    fs.writeFileSync(filePath, JSON.stringify(questions, null, 2), 'utf8');
    return true;
  } catch (error) {
    console.log(`Could not save questions: ${error.message}`);
    return false;
  }
}

// Fisher-Yates shuffle on a copy (original array is untouched).
function shuffleQuestions(questions) {
  const copy = [...questions];
  for (let i = copy.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [copy[i], copy[j]] = [copy[j], copy[i]];
  }
  return copy;
}

module.exports = { loadQuestions, saveQuestions, shuffleQuestions, isValidQuestion, defaultQuestions };
