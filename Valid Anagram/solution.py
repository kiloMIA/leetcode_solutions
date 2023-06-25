class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first_word = set(s)

        if len(s) != len(t):
            return False

        for i in first_word:
            if s.count(i) != t.count(i):
                return False
        return True
