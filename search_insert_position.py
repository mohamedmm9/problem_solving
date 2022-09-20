class Solution(object):
    def searchInsert(self, nums, target):
        if nums[0]>target:
            return 0
        elif nums[len(nums)-1]<target:
            return len(nums)
        else:
            low_index = 0
            high_index = len(nums)-1
            while low_index<=high_index:
                mid_index = low_index+(high_index-low_index)//2
                if nums[mid_index]==target:
                    return mid_index
                elif nums[mid_index]<target:
                    low_index = mid_index+1
                else:
                    high_index = mid_index-1
            return low_index
