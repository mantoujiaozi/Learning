class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
# 记录上下车地点，并遵循先下后上原则，暴力破解车上人数是否大于车内最大可承载量
#         shangche = []
#         xiache = []
#         for i in range(len(trips)):
#             shangche.append(trips[i][1])
#             xiache.append(trips[i][2])

#         c = 0
#         for i in range(1,1000):
#             for j in range(len(trips)):
#                 if xiache[j] == i:
#                     c = c - trips[j][0]
#             for j in range(len(trips)):
#                 if shangche[j] == i:
#                     c = c + trips[j][0]

#             if c > capacity:
#                 return False
        
#         return True

#copy其他人代码，只需用一个list,每一次都更新当前节点下（上车和下车）车内的人数，最后相加人数，看是否超过最大可承载量
        v= [0]*1000
        for i in trips:
            v[i[1]] += i[0]
            v[i[2]] -= i[0]

        temp = 0
        for i in range(1000):
            temp += v[i]
            if temp > capacity:
                return False
            
        return True