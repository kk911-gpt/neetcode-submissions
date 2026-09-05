class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        row=len(matrix)
        col= len(matrix[0])

        row_zero=False
        col_zero= False

        for r in range (row):
            if matrix[r][0]==0:
                col_zero= True
        for c in range(col):
            if matrix[0][c]==0:
                row_zero= True

        for r in range(1,row):
            for c in range(1,col):
                if matrix[r][c]==0:
                    matrix[r][0]=0
                    matrix[0][c]=0

        for r in range(1,row):
            for c in range(1, col):
                if matrix[r][0]==0 or matrix[0][c]==0:
                    matrix[r][c]=0
        
        if row_zero:
            for c in range(col):
                matrix[0][c]=0
        if col_zero:
            for r in range(row):
                matrix[r][0]=0