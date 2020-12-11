/**
 Task. Given two integers 𝑛 and 𝑚, output 𝐹𝑛 mod 𝑚 (that is, the remainder of 𝐹𝑛 when divided by 𝑚).
 Input Format. The input consists of two integers 𝑛 and 𝑚 given on the same line (separated by a space).
 Constraints. 1≤𝑛≤1014,2≤𝑚≤103.
 Output Format. Output 𝐹𝑛 mod 𝑚.
 Sample 1.
 Input: 239 1000
 Output: 161
 𝐹239 mod 1000 = 39679027332006820581608740953902289877834488152161 (mod 1000) = 161.
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
    const n = parseInt(line.toString().split(' ')[0], 10);
    const m = parseInt(line.toString().split(' ')[1], 10);

    console.log(getFibMod(n, m));
    process.exit();
  }
}

function seqLength (m) {
  let prev = 0, cur = 1;

  for (let i = 1; i < m * m; i++) {
    let t = cur;
    cur = (cur + prev) % m;
    prev = t;
    if (cur === 1 && prev === 0) {
      return i;
    }
  }
  return 0;
}

function getFibMod (n, m) {

  let prev = 0, cur = 1;
  let len = seqLength(m);

  n = n % len;

  if (n <= 1)
    return n;

  for (let i = 0; i < n - 1; i++) {
    let t = cur;
    cur = (cur + prev) % m;
    prev = t;
  }
  return cur % m;
}

module.exports = getFibMod;
