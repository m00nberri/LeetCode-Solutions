/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    for (i = 0; i < nums.length; i++) {
        for (n = 0; n < nums.length; n++) {
            if (i === n) {
                continue
            }
            else if (parseInt(nums[i] + nums[n]) === target) {
                let targetPair = [i,n];
                return targetPair;
            }
            else {
                continue
            }
        }
    }
};