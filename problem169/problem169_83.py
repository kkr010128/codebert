n = int(input())
alist = list(map(int,input().split()))
syain = [0]*n
for i in range(n-1):
    syain[alist[i]-1] += 1
for i in range(n):
    print(syain[i])