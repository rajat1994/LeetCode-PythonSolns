class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst = {}
        
        for i in range(0,len(nums)):
            if target - nums[i] in lst and lst[target - nums[i]] != i:
                return [lst[target-nums[i]],i]
            
            else:
                lst[nums[i]] = i
            
            