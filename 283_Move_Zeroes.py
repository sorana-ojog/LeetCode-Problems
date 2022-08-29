'''
Given an integer array nums, move all 0's to the end of it
while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastSwapPos = 0
        # for i, x in list(filter(lambda i : i[1] != 0, enumerate(nums))):
        for i, x in enumerate(nums):
            if x != 0:
                nums[lastSwapPos], nums[i] = nums[i], nums[lastSwapPos]
                lastSwapPos += 1
                
'''
Time Complexity: O(n)
Space Complexity: O(1)
'''
