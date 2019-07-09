import numpy as np

class Solution(object):
     
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
#         求去A地和B地的差值，并得到排序的索引，每次取一个最大和最小的值
#         minus = []
#         cost = 0
#         N = len(costs)
#         minus = [i[0] - i[1] for i in costs]
            
#         index = np.argsort(minus)
#         for i in range(int(N/2)):
#             cost = cost + costs[index[i]][0] + costs[index[N-i-1]][1]
        
#       直接得到差值排序后的costs值，去A城的取前1/2，后1/2去B城
        costs.sort(key=lambda x: (x[0]-x[1]))
        N = len(costs)
        cost = sum(i[0] for i in costs[:N/2])+sum(i[1] for i in costs[N/2:])
        
        return cost