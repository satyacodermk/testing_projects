# Interactive Quiz & Learning App

A beginner-friendly, console-based quiz game built with plain JavaScript (Node.js). No external packages needed.

## Run

```bash
node index.js            # normal order
node index.js --shuffle  # random question order
node tests/testLogic.js  # run the logic tests
```

Requires Node.js 14+.

## Project structure

| File | Responsibility |
|------|----------------|
| `index.js` | **Main script** – entry point, menu and restart loops |
| `modules/questionData.js` | Load/validate questions (`JSON.parse`), save (`JSON.stringify`), shuffle |
| `modules/menu.js` | Welcome banner, rules, Start/Exit menu (`switch`) |
| `modules/inputValidation.js` | `askQuestion()` helper, `getValidAnswer()`, y/n and Enter helpers |
| `modules/quiz.js` | `displayQuestion()`, `checkAnswer()`, quiz `for` loop |
| `modules/score.js` | Counters, `calculatePercentage()`, performance message |
| `modules/results.js` | Final results screen |
| `modules/restart.js` | Play-again prompt and goodbye |
| `input/questions.json` | Question bank (edit this to add questions) |
| `tests/testLogic.js` | Manual tests for validation and scoring |

## Adding questions

Add an object to `input/questions.json`:

```json
{
  "question": "Your question?",
  "options": ["A", "B", "C"],
  "correctAnswer": 1
}
```

`correctAnswer` is the **zero-based index** of the right option (`0` = first option). Questions with fewer than 2 options or a bad index are skipped with a note. If the file is missing or broken, built-in questions are used.

## Edge cases handled

Empty input, `0`, out-of-range numbers, decimals, negatives, letters, padded input (`" 3 "`), uppercase `Y`/`N`, two-option questions, empty question list (friendly message), division by zero (0%, never `NaN`), and closed input (Ctrl+D) exits cleanly.
