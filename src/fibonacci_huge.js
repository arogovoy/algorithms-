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
// const readline = require('readline');
// const rl = readline.createInterface({
//   input: process.stdin,
//   terminal: false
// });
//
// process.stdin.setEncoding('utf8');
// rl.on('line', readLine);

function readLine (line) {
  if (line !== '\n') {
    const n = parseInt(line.toString().split(' ')[0], 10);
    const m = parseInt(line.toString().split(' ')[1], 10);

    console.log(getFibMod(n, m));
    process.exit();
  }
}

// console.log(getFibMod(239, 1000))
// console.log(getFibMod(2816213588, 239));

// console.log(getFibMod(13, 3))

function getFibMod (n, m) {
  if (n <= 1)
    return n;

  const indexes = [0, 1];

  let modsLen = 1;
  let i = 2;
  while (i < n && modsLen === 1) {
    indexes.push(indexes[i - 1] + indexes[i - 2]);
    // if (i === 15 /*|| indexes[indexes.length - 1] % m === 1*/) break
    // console.log(indexes[indexes.length - 1] % m, ':' ,  indexes[indexes.length - 2] % m);
    // console.log(indexes);

    if (indexes[indexes.length - 1] % m === 1) {
      console.log(indexes);
    }

    // console.log(indexes[indexes.length - 1], ':' ,  indexes[indexes.length - 1] % m);
    if (indexes[indexes.length - 1] % m === 1 && indexes[indexes.length - 2] % m === 0) {
      modsLen = indexes.length - 2;
    }
    ++i;
  }
  console.log(modsLen);
  return indexes[n - Math.floor(n / modsLen) * modsLen] % m;
}

(()=>{

    let prev = 0;
    let curr = 1;
    let res = 0;
    let n = 13, m = 9;

    for (let i = 0; i < m * m; ++i) {
      console.log(i, i % m);

      let temp = curr;
      curr = (prev + curr) % m;
      prev = temp;

      if (prev === 0 && curr === 1)
        res = i + 1;
    }
    console.log(res);

  }
)()


function pisano (m) {
  let prev = 0;
  let curr = 1;
  let res = 0;

  for (let i = 0; i < m * m; i++) {
    let temp = curr;
    curr = (prev + curr) % m;
    prev = temp;

    if (prev === 0 && curr === 1)
      res = i + 1;
  }
  return res;
}

console.log(pisano(3));

// Calculate Fn mod m
function fibonacciModulo (n,
  m) {

  // Getting the period
  let pisanoPeriod = pisano(m);

  n = n % pisanoPeriod;

  let prev = 0;
  let curr = 1;

  if (n === 0)
    return 0;
  else if (n === 1)
    return 1;

  for (let i = 0; i < n - 1; i++) {
    let temp = 0;
    temp = curr;
    curr = (prev + curr) % m;
    prev = temp;
  }
  return curr % m;
}

module.exports = getFibMod;
