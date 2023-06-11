class Solution:
    def twoSum(self,nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        while left < right:
            twosum = nums[left] + nums[right]
            if target == twosum:
                return [left,right]
            if target > twosum:
                left += 1
            else:
                right -= 1
            
                
                            
