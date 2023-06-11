class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        
        while left < right:
            # Swap the value from left most to right most
            s[left], s[right] = s[right], s[left]
            # Shift the pointers
            left += 1
            right -= 1
