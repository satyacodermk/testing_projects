// Score Management Module
function createScore() {
  return { correct: 0, incorrect: 0 };
}

function recordAnswer(score, isCorrect) {
  if (isCorrect) {
    score.correct += 1;
  } else {
    score.incorrect += 1;
  }
  return score;
}

// Safe percentage: returns 0 when total is 0 (no divide-by-zero / NaN).
function calculatePercentage(correct, total) {
  if (total <= 0) {
    return 0;
  }
  return Math.round((correct / total) * 100);
}

function getPerformanceMessage(percentage) {
  if (percentage >= 90) {
    return 'Excellent! Perfect command of the basics!';
  } else if (percentage >= 70) {
    return 'Great job! You really know your stuff!';
  } else if (percentage >= 50) {
    return "Good effort! A little more practice and you'll master it.";
  } else {
    return "Keep practicing! Every attempt makes you better. You've got this!";
  }
}

module.exports = { createScore, recordAnswer, calculatePercentage, getPerformanceMessage };
