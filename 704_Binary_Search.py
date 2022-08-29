'''Given an array of integers nums which is sorted in ascending order,
and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.rec (0, len(nums)-1, nums, target)
        
    def rec(self, i, j, numbers, target):
        if numbers[i] == target:
            return i
        if numbers[j] == target:
            return j
        if abs(i-j) <= 1:
            return -1
        m = round((i + j)/2)
        if numbers[m] == target:
            return m
        elif numbers[m] < target:
            return self.rec(m, j, numbers, target)
        else:
            return self.rec(i, m, numbers, target)
          
          
'''
Time Complexity: O(log(n))
Space Complexity: O(log(n))
'''
