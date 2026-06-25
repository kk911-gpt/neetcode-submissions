class Solution:
    def hammingWeight(self, n: int) -> int:
        #n= bin(n)[2:]
        #count=0

        #for x in n:
         #   if x== '1':
             #   count+=1
        #return count

        ans=0

        while n!=0:
            ans+=1
            n= n & (n-1)
        return ans 