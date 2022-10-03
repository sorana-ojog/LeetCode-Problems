'''
1578. Minimum Time to Make Rope Colorful

Alice has n balloons arranged on a rope. You are given a 0-indexed string colors 
where colors[i] is the color of the ith balloon.

Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, 
so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given 
a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to 
remove the ith balloon from the rope.

Return the minimum time Bob needs to make the rope colorful.
'''

from math import inf
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        totalNeededTime = 0
        maxTime = 0
        currentSum = 0
        colors += "!"
        
        for i in range(len(colors)-1):
            currentSum += neededTime[i]
            maxTime = max(maxTime, neededTime[i])
            
            if colors[i] != colors[i + 1]:
                if currentSum != neededTime[i]:
                    totalNeededTime += (currentSum - maxTime) 
                currentSum = 0 
                maxTime = 0
                
        return totalNeededTime
        
'''
Time Complexity: O(n)
Space Complexity: O(n^2)
#I think it is possibly O(n^2) because I am adding a character at the end of the string and strings are immutable
REF: https://dock2learn.com/tech/how-to-efficiently-concatenate-strings-in-python/
'''
