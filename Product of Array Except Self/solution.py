from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for num in range(len(nums)):
            res[num] = prefix
            prefix *= nums[num]

        postfix = 1
        for num in range(len(nums) - 1, -1, -1):
            res[num] *= postfix
            postfix *= nums[num]
        return res

#
# if __name__ == '__main__':
#     productExceptSelf([1,2,3,4])