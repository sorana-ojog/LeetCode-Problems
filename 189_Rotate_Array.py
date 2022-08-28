'''
Given an array, rotate the array to the right by k steps, where k is non-negative.
'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(0, k):
            el = nums.pop()
            nums.insert(0, el)
            
'''
Time Complexity: O(k*n)
Space Complexity: O(1)
'''

# Second Solution
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         k = k % len(nums)
#         aux = nums[-k:]
#         nums[k:] = nums[:-k]
#         nums[:k] = aux
# 
# '''
# Time Complexity: O(n)
# Space Complexity: O(1)
# ''' 
