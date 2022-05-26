// How can you make this more scalable and reusable later?

exports.findArmstrongNumbers = function(arrayOfNums) {
    let answerArray = [];
    const tempArray = arrayOfNums.map(element => element.toString().split('').map((num, _, a) => num ** a.length)).map(elem => elem.reduce((a, b) => a + b));
    for (let i = 0; i < arrayOfNums.length; i++) {
        if (arrayOfNums[i] === tempArray[i]) {
            answerArray.push(arrayOfNums[i]);
        }
    }
    return answerArray;
};