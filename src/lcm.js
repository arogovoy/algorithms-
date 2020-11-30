/**
 Task. Given two integers 𝑎 and 𝑏, find their least common multiple.
 Input Format. The two integers 𝑎 and 𝑏 are given in the same line separated by space.
 Constraints. 1 ≤ 𝑎, 𝑏 ≤ 107 .
 Output Format. Output the least common multiple of 𝑎 and 𝑏.
 Sample 1.
 Input:6 8
 Output:24
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

    console.log(lcm(a, b));
    process.exit();
  }
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

function lcm (a, b) {
  return (a * b) / gcd(a, b);
}

module.exports = lcm;
