import math
# a=int(input())
#b=int(input())
# c=[]
# for i in b:
#     c.append(i)
e1,e2 = map(int,input().split())
f = list(map(int,input().split()))
#j = [input() for _ in range(3)]
cal=1
for i in range(e1-e2):
    if f[i]>=f[i+e2]:
        print("No")
    else:
        print("Yes")