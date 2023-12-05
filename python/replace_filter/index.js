Array.prototype.remove = function (pred) {
    const removed = [];
    let writeIndex = 0;
    for(let readIndex = 0; readIndex < this.length; readIndex++) {
        if(pred(this[readIndex])) {
            removed.push(this[readIndex]);
        } else {
            if(writeIndex !== readIndex){
                this[writeIndex] = this[readIndex];
            }
            writeIndex++;
        }
    }
    this.length = writeIndex;
    return removed;
};

const myArray = [0, 1, 2, 3, 4, 5];
removed = myArray.remove(function(a) { return a%2===0;});
console.log(myArray);
console.log(removed);

var array = [1,2,3,4,5];
var predicate = i => i % 2 === 0;
var removed = array.remove(predicate);
console.log('SB [2,4] is ' + removed);
console.log('SB [1,3,5] is ' + array);

array = [1,2,3,4,5];
predicate = i => i % 2 !== 0;
removed = array.remove(predicate);
console.log('SB [1,3,5] is ' + removed);
console.log('SB [2,4] is ' + array);

array = [2,2,2,2,2];
predicate = i => i === 2;
removed = array.remove(predicate);
console.log('SB [2,2,2,2,2] is ' + removed);
console.log('SB [] is ' + array);

array = ['a', 'b', 'c', 'd', 'e'];
predicate = i => i >= 'a' && i <= 'd';
removed = array.remove(predicate);
console.log('SB [\'a\', \'b\', \'c\', \'d\'] is ' + removed);
console.log('SB [\'e\'] is ' + array);


