class Solution:
    def reverse(self, x: int) -> int:
        sign= -1 if x< 0 else 1
        x= abs(x)

        res=0
        MAX= 2**31-1

        while x:
            digit= x%10
            x= x//10

            if res> MAX//10:
                return 0

            if res== MAX//10 and digit > MAX % 10:
                return 0
            
            res= res *10 +digit
        return  sign * res