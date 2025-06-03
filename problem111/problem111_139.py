import copy
n = int(input())
a = list(map(int,input().split()))
a.sort(reverse=True)
count = 0
for i in range(len(a)-1):
    count += a[(i+1)//2]
print(count)