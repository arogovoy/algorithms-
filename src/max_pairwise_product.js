/**
 Maximum Pairwise Product Problem
 Find the maximum product of two distinct numbers in a sequence of non-negative integers.
 Input: A sequence of non-negative integers.
 Output: The maximum value that can be obtained by multiplying two different elements from the sequence.

 Input:
 7 5 14 2 8 8 10 1 2 3
 Output:
 140
 */

const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    terminal: false
});

process.stdin.setEncoding('utf8');
rl.once('line', () => {
    rl.on('line', readLine);
});

function readLine (line) {
    const arr = line.toString().split(' ').map(Number);

    console.log(max(arr));
    process.exit();
}

function max(arr) {
    let maxIndex1 = 0, maxIndex2 = -1;
    for (let i = 1; i < arr.length; i++) {
        if (arr[i] > arr[maxIndex1])
            maxIndex1 = i;
    }

    for (let i = 0; i < arr.length; i++) {
        if (maxIndex1 !== i && (maxIndex2 === -1 || arr[i] > arr[maxIndex2])) {
            maxIndex2 = i;
        }
    }
    return arr[maxIndex2] * arr[maxIndex1];
}

module.exports = max;
