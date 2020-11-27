/**
 * Task. Given an integer 𝑛, find the last digit of the 𝑛th Fibonacci number 𝐹𝑛 (that is, 𝐹𝑛 mod 10).
 * Input Format. The input consists of a single integer 𝑛.
 * Constraints. 0 ≤ 𝑛 ≤ 107.
 * Output Format. Output the last digit of 𝐹𝑛.
 *
 * Sample 2.
   Input: 331
   Output: 9
   𝐹331 = 668996615388005031531000081241745415306766517246774551964595292186469.
 */

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    terminal: false
});

process.stdin.setEncoding('utf8');
rl.on('line', readLine);

function readLine(line) {
    console.log(fib(parseInt(line, 10)));
    process.exit();
}

function fib (n) {
    const indexes = [0, 1];

    for (let i = 2; i < n; i++) {
        indexes.push((indexes[i - 1] + indexes[i - 2]) % 10);
    }
    return (indexes[n - 1] + indexes[n - 2]);
}

module.exports = fib;
