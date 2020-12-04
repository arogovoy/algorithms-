/**
 Task. Compute the last digit of 𝐹02 +𝐹12 +···+𝐹𝑛2.
 Input Format. Integer 𝑛.
 Constraints. 0 ≤ 𝑛 ≤ 10^14.
 Output Format. The last digit of 𝐹0^2 + 𝐹1^2 + · · · + 𝐹𝑛^2.
 Sample 1.
 Input: 7
 Output: 3
 𝐹02 +𝐹12 +···+𝐹72 =0+1+1+4+9+25+64+169=273.
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

    console.log(fibonacci_sum_squares(n));
    process.exit();
  }
}

function fibonacci_sum_squares (n) {
  let prev = 0, cur = 1, res = 1;
  const pisanoPeriod = 60;

  n = n % pisanoPeriod;

  if (n <= 1)
    return n;

  for (let i = 0; i < n - 1; i++) {
    let t = cur;
    cur = (cur + prev) % 10;
    prev = t;
    res += cur * cur;
  }
  return res % 10;
}

module.exports = fibonacci_sum_squares;
