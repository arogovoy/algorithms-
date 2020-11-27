const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  terminal: false
});

process.stdin.setEncoding('utf8');
rl.on('line', readLine);

function readLine (line) {
  console.log(fib(parseInt(line, 10)));
  process.exit();
}

function fib2 (n) {
  if (n <= 1)
    return n;

  return fib(n - 1) + fib(n - 2);
}

function fib (n) {
  const indexes = [0, 1];

  for (let i = 2; i < n; i++) {
    indexes.push(indexes[i - 1] + indexes[i - 2]);
  }
  return indexes[n - 1] + indexes[n - 2];
}

module.exports = fib;
