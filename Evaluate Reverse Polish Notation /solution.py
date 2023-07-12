from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['/', '*', '-', '+']

        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                first = int(stack.pop())
                second = int(stack.pop())
                if t == '+':
                    stack.append(first + second)
                elif t == '-':
                    stack.append(second - first)
                elif t == '*':
                    stack.append(first * second)
                else:
                    stack.append(second / first)
        return int(stack[-1])

