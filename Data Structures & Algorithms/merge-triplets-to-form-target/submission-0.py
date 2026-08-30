class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        current=[0,0,0]

        for triplet in triplets:
            if triplet[0]>target[0] or triplet[1]> target[1] or triplet[2]> target[2]:
                continue

            
            current[0]= max( current[0], triplet[0])
            current[1]= max(current[1], triplet[1])
            current[2]= max( current[2], triplet[2])
        return current== target