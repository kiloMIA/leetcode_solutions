from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicti = {}

        for i in range(len(nums)):
            dicti[nums[i]] = i

        for i in range(len(nums)):
            current_num = target - nums[i]
            if current_num in dicti and dicti[current_num] != i:
                return[i, dicti[current_num]]
        return []