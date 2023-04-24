/**
 * Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.
 * Return the positive integer k. If there is no such integer, return -1.
 
 * @param {number[]} nums
 * @return {number}
 */
var findMaxK = function(nums) {
    nums.sort((a, b) => a - b);
    var i = 0;
    var j = nums.length - 1;
    while(nums[i] < nums[j]){
        if(nums[i] * (-1) == nums[j]){
            return nums[j];
        } else if (nums[i] * (-1) < nums[j]){
            j--;
        } else if (nums[i] * (-1) > nums[j]){
            i++;
        }
    }
    return -1;
};


// Time Complexity: O(n*log(n)) - taking into consideration that the JS sort method is O(n*log(n))
// Space Complexity: O(1)
