from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = []
        current_sum = 0
        for num in nums:
            current_sum += num
            self.prefix_sum.append(current_sum)

    def sumRange(self, left: int, right: int) -> int:
        r = self.prefix_sum[right]
        if left > 0:
            l = self.prefix_sum[left - 1]
        else:
            l = 0
        return r - l
