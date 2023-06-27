from typing import List



def topKFrequent(nums: List[int], k: int) -> List[int]:
    frequent_elements = {}
    elements_set = set(nums)
    # empty_str = ''
    # str_list = empty_str.join(str(num) for num in nums)

    for element in elements_set:
        frequency = nums.count(element)
        frequent_elements[element] = frequency

    sorted_elements = sorted(frequent_elements.items(), key=lambda x: x[1], reverse=True)
    most_frequent = [element for element, frequency in sorted_elements[:k]]


    return most_frequent


if __name__ == '__main__':
    topKFrequent([4,1,-1,2,-1,2,3], 2)