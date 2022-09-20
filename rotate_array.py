class Solution(object):
    def rotate(self, nums, k):
        k = k%len(nums)
        k=len(nums)-k
        nums[::] = nums[k:]+nums[:k] 
