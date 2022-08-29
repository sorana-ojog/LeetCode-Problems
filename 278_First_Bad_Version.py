'''
You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check. 
Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, 
which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. 
Implement a function to find the first bad version. You should minimize the number of calls to the API.
'''

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if isBadVersion(0):
            return 0
        return self.rec (0, n)
        
    def rec(self, i, j):
        if abs(i-j) <= 1:
            if isBadVersion(i):
                return i
            else:
                return j
        m = round((i + j)/2)
        if isBadVersion(m):
            if isBadVersion(m-1) is False:
                return m
            else:
                return self.rec(i, m)
        else:
            return self.rec(m, j)
            
'''
Time Complexity: O(log(n))
Space Complexity: O(log(n))
'''
