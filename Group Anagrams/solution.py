from operator import countOf
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagram_dict = {}
    empty_str = ''

    for anagram in strs:
        temp = empty_str.join(sorted(anagram))
        print(temp)
        if temp in anagram_dict:
            anagram_dict[temp].append(anagram)
        else:
            anagram_dict[temp] = [anagram]

    print(list(anagram_dict.values()))

    return list(anagram_dict.values())


if __name__ == '__main__':
    groupAnagrams(["eat","tea","tan","ate","nat","bat"])