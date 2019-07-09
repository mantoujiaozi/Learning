import heapq 

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse=True)
        N = len(stones)
 
        while N > 2 :
            temp = stones[0] - stones[1]
            stones.remove(stones[0])
            stones.remove(stones[0])
            if temp == 0:
                N = N-2
            else:
                stones.append(temp)
                stones.sort(reverse=True)
                N = len(stones)
         
        N = len(stones)
        if N == 2:
            if abs(stones[0] - stones[1])>0 :
                y = abs(stones[0] - stones[1])
            else:
                y = 0
        else :
            y = stones[0]

        return y