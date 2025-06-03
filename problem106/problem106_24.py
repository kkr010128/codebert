import numpy as np

N = int(input())
#N,K,d= map(int,input().split())
#A = list(map(int,input().split()))
#S = str(input())
#T = str(input())

num=np.zeros(10**4+1)
for x in range(1,100):
    for y in range(1,100):
        for z in range(1,100):
            ans = x**2 + y**2 + z**2 + x*y + y*z + z*x
            if ans < 10**4+1:
                num[ans]+=1


for i in range(N):
    print(int(num[i+1]))
