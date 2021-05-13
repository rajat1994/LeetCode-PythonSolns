class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        if target < nums[0]:
            return 0
        
        if target > nums[len(nums)-1]:
            return len(nums)
        
        first = 0
        last = len(nums)-1
        
        while first <= last :
            
            mid = (first + last)//2
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                first = mid + 1
                
            else:
                last = mid -1
                
        return first
        