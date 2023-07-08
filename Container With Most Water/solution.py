from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left = 0
        right = len(height) - 1
        while left < right:
            if height[left] < height[right]:
                current_res = (right - left) * height[left]
                left += 1
            else:
                current_res = (right - left) * height[right]
                right -= 1
            res = max(res, current_res)
        return res
