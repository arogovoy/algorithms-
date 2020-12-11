/**
 Task. Given two integers 𝑎 and 𝑏, find their greatest common divisor.
 Input Format. The two integers 𝑎, 𝑏 are given in the same line separated by space.
 Constraints. 1≤𝑎,𝑏≤2·10^9.

 Sample 2.
 Input: 28851538 1183019
 Output: 17657
 28851538 = 17657 · 1634, 1183019 = 17657 · 67.
 */

const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  terminal: false
});

process.stdin.setEncoding('utf8');
rl.on('line', readLine);

function readLine (line) {
  if (line !== '\n') {
    const a = parseInt(line.toString().split(' ')[0], 10);
    const b = parseInt(line.toString().split(' ')[1], 10);

    console.log(gcd(a, b));
    process.exit();
  }
}

function gcd2 (a, b) {
  if (b < a) {
    let t = b;
    b = a;
    a = t; //a is always min
  }

  let result = a;
  while (result > 1 && (a / result % 1) || (b / result % 1)) {
    --result;
  }
  return result;
}

function gcd (a, b) {
  if (b > a) {
    let t = a;
    a = b;
    b = t; //b is always min
  }

  if (b === 0) {
    return a;
  }

  return gcd(a % b, b);
}

module.exports = gcd;
