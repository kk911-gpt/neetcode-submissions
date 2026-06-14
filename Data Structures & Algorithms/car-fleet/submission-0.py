class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars= list(zip(position,speed))

        cars.sort()
        stk=[]

        for p,s in reversed(cars):
            time = (target - p)/s

            if stk and time <= stk[-1]:
                continue
            stk.append(time)
        return len(stk)