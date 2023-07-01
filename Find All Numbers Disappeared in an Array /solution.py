from typing import List


def findDisappearedNumbers(nums: List[int]) -> List[int]:
        number_hash = {}
        nums.sort()
        for i in range(1, len(nums) + 1):
            number_hash[i] = None

        for num in nums:
            number_hash[num] = num

        result = []
        for num, value in number_hash.items():
            if value is None:
                result.append(num)

        return result


if __name__ == '__main__':
    findDisappearedNumbers([4,3,2,7,8,2,3,1])