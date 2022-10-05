class Solution:
    def findPeakElement(self,nums):
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return 0
        
        left = 0 
        right = len(nums)-1 
        
        while left <= right:
            mid = (left + right)//2 # middle 
            
            left_mid = nums[mid-1] if mid > 0 else float("-inf")
            
            right_mid= nums[mid+1] if mid < len(nums)-1 else float("-inf")
            
            if nums[mid] >  left_mid and nums[mid] > right_mid:
                return mid
            
            elif left_mid < nums[mid] < right_mid:
                left = mid+1 
            
            else: 
                right = mid-1  
