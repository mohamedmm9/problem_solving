class Solution(object):
    def searchMatrix(self, matrix, target):
        res = any(target in sub for sub in matrix)
        return res
