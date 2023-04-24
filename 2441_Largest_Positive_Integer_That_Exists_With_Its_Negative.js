/**
 * Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.
 * Return the positive integer k. If there is no such integer, return -1.
 
 * @param {number[]} nums
 * @return {number}
 */

//Method 1: with lower space complexity (sorting the numbers)

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



//Method 2: with lower time complexity (implementing a hash table)

var findMaxK = function(nums) {
    var table = {}
    var max = 0;
    for ( let i = 0; i < nums.length; i++){
        table[nums[i]] = nums[i]
        if (table[nums[i] * (-1)] !== undefined){
            if (max < Math.abs(nums[i])){
                max = Math.abs(nums[i])
            }
        }
    }
    if (max === 0){
        return -1
    }
    return max;
};

// Time Complexity: O(n) - n* O(1) for every lookup into the table
// Space Complexity: O(n) - n* O(1) for every addition into the hash table
