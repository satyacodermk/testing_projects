// Input Validation Module: ONE reusable input helper + validators.
const fs = require('fs');

let buffer = '';
let inputEnded = false;

function sleep(ms) {
  Atomics.wait(new Int32Array(new SharedArrayBuffer(4)), 0, 0, ms);
}

// Reads one line from stdin synchronously (works typed or piped).
function readLine() {
  while (true) {
    const newlineIndex = buffer.indexOf('\n');
    if (newlineIndex !== -1) {
      const line = buffer.slice(0, newlineIndex);
      buffer = buffer.slice(newlineIndex + 1);
      return line.replace(/\r$/, '');
    }
    if (inputEnded) {
      if (buffer.length > 0) {
        const last = buffer;
        buffer = '';
        return last;
      }
      throw new Error('INPUT_CLOSED');
    }
    const chunk = Buffer.alloc(1024);
    let bytesRead = 0;
    try {
      bytesRead = fs.readSync(0, chunk, 0, chunk.length, null);
    } catch (error) {
      if (error.code === 'EAGAIN') {
        sleep(50);
        continue;
      }
      if (error.code !== 'EOF') {
        throw error;
      }
    }
    if (bytesRead === 0) {
      inputEnded = true;
    } else {
      buffer += chunk.toString('utf8', 0, bytesRead);
    }
  }
}

// The single helper every other module uses to talk to the user.
function askQuestion(prompt) {
  process.stdout.write(prompt);
  return readLine();
}

// Converts raw text into an option number, or returns null if invalid.
// Rejects: empty, letters, decimals (2.5), negatives, zero, out of range.
function parseOptionNumber(rawInput, maxOption) {
  const text = String(rawInput).trim();
  if (!/^\d+$/.test(text)) {
    return null;
  }
  const number = Number(text);
  if (!Number.isInteger(number) || number < 1 || number > maxOption) {
    return null;
  }
  return number;
}

// Keeps asking until the user types a valid option number (1..optionCount).
function getValidAnswer(optionCount) {
  while (true) {
    const raw = askQuestion(`Enter your answer (1-${optionCount}): `);
    const number = parseOptionNumber(raw, optionCount);
    if (number !== null) {
      return number;
    }
    console.log(`\nInvalid input. Please enter a number between 1 and ${optionCount}.\n`);
  }
}

// Menu choice must be 1 or 2.
function getValidMenuChoice() {
  while (true) {
    const raw = askQuestion('Enter your choice: ');
    const number = parseOptionNumber(raw, 2);
    if (number !== null) {
      return number;
    }
    console.log('\nInvalid choice. Please enter 1 or 2.\n');
  }
}

// Accepts y / yes / n / no in any letter case. Returns true for yes.
function getYesNo(prompt) {
  while (true) {
    const answer = askQuestion(prompt).trim().toLowerCase();
    if (answer === 'y' || answer === 'yes') return true;
    if (answer === 'n' || answer === 'no') return false;
    console.log('Invalid input. Please type y or n.');
  }
}

function waitForEnter(prompt = 'Press Enter to continue...') {
  askQuestion(`\n${prompt}`);
}

module.exports = { askQuestion, parseOptionNumber, getValidAnswer, getValidMenuChoice, getYesNo, waitForEnter };
