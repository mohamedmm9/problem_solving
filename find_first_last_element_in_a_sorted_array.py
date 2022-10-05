class Solution:
    def searchRange(self,N,T):
        def find(target, arr, left=0):
            right = len(arr) - 1
            while left <= right:
                mid = left + right >> 1
                if arr[mid] < target: left = mid + 1
                else: right = mid - 1
            return left
        Tleft = find(T, N)
        if Tleft == len(N) or N[Tleft] != T: return [-1, -1]
        return [Tleft, find(T+1, N, Tleft) - 1]
