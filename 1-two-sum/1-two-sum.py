class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for n in nums:
            if target - n in nums[nums.index(n)+1:]:
                return [nums.index(n),len(nums)-(nums[::-1].index(target-n))-1]
        
        return [69]