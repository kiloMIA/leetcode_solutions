from typing import List


def singleNumber(nums: List[int]) -> int:
    xor = 0
    for num in nums:
        xor ^= num
        print(xor)
    print(xor)
    return xor


if __name__ == '__main__':
    singleNumber([4,1,2,1,2])