/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let forward = (x.toString()).split('');
    let copy = (x.toString()).split('');
    let backward = [];
    for (i = 1; i <= forward.length; i++) {
        backward.push(copy.pop());
        if (((forward.slice(0,i)).join()) !== backward.join()) {
            return false;
        }
        else {
            continue;
        }
    }
    return true;
};