const fs = require('fs');
// import fs from 'fs';

// Load wordlist from JSON file
const wordlistData = fs.readFileSync('wordlistbig.json');
const wordlistJson = JSON.parse(wordlistData);
const wordlist = wordlistJson.wordlist;


// Filter functions
const filterWordsByLength = (words, length) => {
    return words.filter(word => word.length === length);
};

const filterWordsExcludingLetters = (words, excludeLetters) => {
    return words.filter(word => !excludeLetters.some(letter => word.includes(letter)));
};

const filterWordsIncludingLetters = (words, includeLetters) => {
    return words.filter(word => [...includeLetters].every(letter => word.includes(letter)));
};

const filterWordsByPosition = (words, positionDict) => {
    return words.filter(word => Object.entries(positionDict).every(([pos, letter]) => word[pos] === letter));
};

const filterWordsNotInPosition = (words, notPositionDict) => {
    return words.filter(word => Object.entries(notPositionDict).every(([pos, letter]) => word[pos] !== letter));
};

// Example usage
const desiredLength = 5;
const excludeLetters = [];
const includeLetters = new Set(['c', 'e', 'i']); // Ensure includeLetters is a Set
const positionDict = { 4: 'e', 2: 'i', 3: 'c' };
const notPositionDict = { 0: 'c', 2: 'c', 1: 'i' };

// Creating list
// First filter by length
let filteredWords = filterWordsByLength(wordlist, desiredLength);

// Then filter by excluding letters
filteredWords = filterWordsExcludingLetters(filteredWords, excludeLetters);

// Then filter by including letters
filteredWords = filterWordsIncludingLetters(filteredWords, includeLetters);

// Then filter by specific positions
filteredWords = filterWordsByPosition(filteredWords, positionDict);

// Finally, filter by not specific positions
const finalList = filterWordsNotInPosition(filteredWords, notPositionDict);

console.log(finalList);