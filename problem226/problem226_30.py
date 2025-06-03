import math

h,n = map(int,input().split())
sum = 0

li = list(map(int,input().split()))

for val in li:
    sum += val

if sum >= h:
    print("Yes")
else:
    print("No")
