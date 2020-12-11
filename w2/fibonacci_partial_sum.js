/**
 Task. Given two non-negative integers 𝑚 and 𝑛, where 𝑚 ≤ 𝑛, find the last digit of the sum 𝐹𝑚 + 𝐹𝑚+1 + ···+𝐹𝑛.
 Input Format. The input consists of two non-negative integers 𝑚 and 𝑛 separated by a space. Constraints. 0 ≤ 𝑚 ≤ 𝑛 ≤ 10^14.
 Output Format. Output the last digit of 𝐹𝑚 + 𝐹𝑚+1 + · · · + 𝐹𝑛.
 Sample 1.
 Input: 3 7
 Output: 1
 𝐹3 +𝐹4 +𝐹5 +𝐹6 +𝐹7 =2+3+5+8+13=31.
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
    const m = parseInt(line.toString().split(' ')[0], 10);
    const n = parseInt(line.toString().split(' ')[1], 10);

    console.log(fibonacci_partial_sum(m, n));
    process.exit();
  }
}

// console.log(fibonacci_partial_sum(1, 2), 2);
// console.log(fibonacci_partial_sum(1, 3), 4);
// console.log(fibonacci_partial_sum(3, 7), 1);
// console.log(fibonacci_partial_sum(10, 10), 5);
// console.log(fibonacci_partial_sum(10, 200), 2);
// console.log(fibonacci_partial_sum(0, 239), 0);
// console.log(fibonacci_partial_sum(1234, 12345), 8);
// console.log(fibonacci_partial_sum(5618252, 6583591534156), 6);

function fibonacci_partial_sum (m, n) {

  let prev = 0, cur = 1, res = 0;
  const pisanoPeriod = 60;

  n = n % pisanoPeriod;
  m = m % pisanoPeriod;

  n = m > n ? n + pisanoPeriod : n;

  if (n <= 1)
    return n;

  for (let i = 0; i < n - 1; i++) {
    let t = cur;
    cur = (cur + prev) % 10;
    prev = t;
    if (i + 2 >= m) {
      res += cur;
    }
  }
  return m <= 2 ? (res + 1) % 10 : res % 10;
}

module.exports = fibonacci_partial_sum;
