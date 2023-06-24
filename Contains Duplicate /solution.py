from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_size = len(nums)
        set_size = len(set(nums))
        if set_size != num_size:
            return True
        else:
            return False