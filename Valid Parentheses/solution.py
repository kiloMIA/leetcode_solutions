class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char not in pairs:
                stack.append(char)
                continue
            elif not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
        return len(stack) == 0


