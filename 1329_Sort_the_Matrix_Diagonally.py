'''
A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost 
row or leftmost column and going in the bottom-right direction until reaching the matrix's end. 
For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, 
includes cells mat[2][0], mat[3][1], and mat[4][2].

Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order 
and return the resulting matrix.
'''

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        self.sortHalf(0,m,0,mat,m,n) #sorting lower half of the matrix
        self.sortHalf(1,n,1,mat,m,n) #sorting upper half of the matrix
        return mat
    
    def sortHalf(self,a,b,c, mat, m,n):
        for x in range(a,b):
            arr = list()
            i,j = self.initialiseIJ(x,c)
            
            while i < m and j < n:
                arr.append(mat[i][j])
                i, j = i + 1, j + 1
            print(arr)
            arr.sort() #should use a better sort method
            
            i,j = self.initialiseIJ(x,c)
            e = 0
            while i < m and j < n:
                mat[i][j] = arr[e]
                i, j, e = i + 1, j + 1, e + 1
    
    def initialiseIJ(self,x,c):
        #depends if we are looking at the upper/lower half
        if(c == 0): 
            i = x
            j = 0
        else:
            i = 0
            j = x
        return (i,j)
        
# My First Try
# class Solution:
#     def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
#         m = len(mat)
#         n = len(mat[0])
#         for x in range(m):
#             arr = list()
#             i = x
#             j = 0
#             while i < m and j < n:
#                 arr.append(mat[i][j])
#                 i, j = i + 1, j + 1
#             print(arr)
#             arr.sort()
            
#             i = x
#             j = 0
#             while i < m and j < n:
#                 mat[i][j] = arr[j]
#                 i, j = i + 1, j + 1
                
#         for x in range(1, n):
#             arr = list()
#             i = 0
#             j = x
#             while i < m and j < n:
#                 arr.append(mat[i][j])
#                 i, j = i + 1, j + 1
#             print(arr)
#             arr.sort()
            
#             i = 0
#             j = x
#             while i < m and j < n:
#                 mat[i][j] = arr[i]
#                 i, j = i + 1, j + 1
#         return mat


'''
Time Complexity: (m+n)*min(m,n)*log(min(m,n)) #I think
Space Complexity: min(m,n) #I think
'''
