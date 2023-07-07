from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution_list = []
        nums.sort()

        for target in range(len(nums)):
            if target > 0 and nums[target] == nums[target - 1]:
                continue

            left = target + 1
            right = len(nums) - 1

            while left < right:
                threeSum = nums[target] + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    solution_list.append([nums[target], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return solution_list
