class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows= len(matrix)
        cols= len(matrix[0])

        left=0
        right= rows*cols -1

        while left <= right:

            middle= (right + left)//2

            row= middle // cols
            col= middle % cols

            num= matrix[row][col]

            if num== target:
                return True
            elif num < target:
                left = middle +1
            else:
                right= middle -1
        return False 