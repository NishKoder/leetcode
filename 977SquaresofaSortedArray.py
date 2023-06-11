class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        result = [0] * len(nums)
        for i in range(len(nums) - 1,-1,-1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
            result[i] = square * square

        return result

# Complexity Analysis

# Time Complexity: O(N), where N is the length of A.

# Space Complexity: O(N) if you take output into account and O(1) otherwise.
