# coding: utf-8
# Your code here!
INF = 2000000000

def getTheNumberOfCoin():
    for i in range(n + 1):
        T.append(INF)
    T[0] = 0
    
    for i in range(m):
        for j in range(C[i], n + 1):
            T[j] = min(T[j], T[j-C[i]] + 1)
    
    return T




T = []
C = []
nums=list(map(int,input().split()))
n = nums[0]
m = nums[1]
nums=list(map(int,input().split()))
for i in range(m):
    C.append(nums[i])

getTheNumberOfCoin()
print(T[n])





