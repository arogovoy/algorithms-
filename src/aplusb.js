const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.on('line', function (line) {
  const result = line.split(' ')
    .reduce((a, b) => Number.parseFloat(a) + Number.parseFloat(b));
  console.log(result);
  process.exit(0);
});
