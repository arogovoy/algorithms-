/**
 Task. Given an integer 𝑛, find the last digit of the sum 𝐹0 +𝐹1 +···+𝐹𝑛.
 Input Format. The input consists of a single integer 𝑛.
 Constraints. 0 ≤ 𝑛 ≤ 10^14.
 Output Format. Output the last digit of 𝐹0 + 𝐹1 + · · · + 𝐹𝑛.
 Sample 1.
 Input: 3
 Output: 4
 𝐹0 +𝐹1 +𝐹2 +𝐹3 =0+1+1+2=4.
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
    const n = parseInt(line.toString(), 10);

    console.log(fibonacci_sum_last_digit(n));
    process.exit();
  }
}

function fibonacci_sum_last_digit (n) {

  let prev = 0, cur = 1, res = 1;
  const pisanoPeriod = 60;

  n = n % pisanoPeriod;

  if (n <= 1)
    return n;

  for (let i = 0; i < n - 1; i++) {
    let t = cur;
    cur = (cur + prev) % 10;
    prev = t;
    res += cur;
  }
  return res % 10;
}

module.exports = fibonacci_sum_last_digit;
