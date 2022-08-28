'''
Given a sorted array of distinct integers and a target value, 
return the index if the target is found. If not, 
return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.rec (0, len(nums)-1, nums, target)
        
    def rec(self, i, j, numbers, target):
        if numbers[i] == target:
            return i
        if numbers[j] == target:
            return j
        if abs(i-j) <= 1:
            if target > numbers[j]:
                return j+1
            elif target < numbers[i]:
                return i
            else:
                return j
        m = round((i + j)/2)
        if numbers[m] == target:
            return m
        elif numbers[m] < target:
            return self.rec(m, j, numbers, target)
        else:
            return self.rec(i, m, numbers, target)
