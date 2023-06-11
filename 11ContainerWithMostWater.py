class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxarea = 0
        while left < right:
            maxarea = max(maxarea, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxarea
  
  
  # Approuch 2 with bruteforce
  class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        for left in range(len(height)):
            for right in range(left + 1,len(height)):
                maxarea = max(maxarea, min(height[left], height[right]) * (right - left))
        return maxarea
