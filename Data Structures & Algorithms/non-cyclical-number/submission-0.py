class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen= set()

        while n!=1:
            if n in seen:
                return False
            seen.add(n)

            summ=0
            while n:
                digit= n % 10
                summ+= digit*digit
                n= n//10
            n=summ
        return True