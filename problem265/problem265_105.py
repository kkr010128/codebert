import math
N=int(input())
l=N*100/108
r=(N+1)*100/108
for i in range(math.ceil(l),math.ceil(r)):
    print(i);exit()
print(":(")
