'''
Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.
'''

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for index, x in enumerate(nums):
            if x >= 0:
                break
        i, j = index - 1, index
        out = []
        while i >= 0 and j <= len(nums) -1:
            if nums[i]**2 <= nums[j]**2:
                out.append(nums[i]**2)
                i -= 1
            else:
                out.append(nums[j]**2)
                j += 1
        while i == -1 and j <= len(nums) -1:
            out.append(nums[j]**2)
            j += 1
        while i >= 0 and j == len(nums):
            out.append(nums[i]**2)
            i -= 1
        return out
