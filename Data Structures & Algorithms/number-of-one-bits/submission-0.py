class Solution:
    def hammingWeight(self, n: int) -> int:
        n= bin(n)[2:]
        count=0

        for x in n:
            if x== '1':
                count+=1
        return count