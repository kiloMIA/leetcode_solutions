from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        left = 0
        right = row * col - 1

        while left <= right:
            piv = (left + right) // 2
            piv_x = piv // col
            piv_y = piv % col

            if matrix[piv_x][piv_y] == target:
                return True
            elif matrix[piv_x][piv_y] < target:
                left = piv + 1
            else:
                right = piv - 1

        return False