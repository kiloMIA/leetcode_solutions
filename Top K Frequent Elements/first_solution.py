from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent_elements = {}

        for num in nums:
            if num in frequent_elements:
                frequent_elements[num] += 1
            else:
                frequent_elements[num] = 1

        sorted_elements = sorted(frequent_elements.items(), key=lambda x: x[1], reverse=True)
        most_frequent = [element for element, frequency in sorted_elements[:k]]

        return most_frequent