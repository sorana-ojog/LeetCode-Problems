'''
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number. Let these two numbers 
be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array 
[index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the 
same element twice.

Your solution must use only constant extra space.
'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            x = self.rec(i +1 ,len(numbers)-1, numbers, target- numbers[i])
            if x != -1:
                return [i+1,x+1]

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
Time Complexity: O(n*log(n))
Space Complexity: O(log(n))
'''
