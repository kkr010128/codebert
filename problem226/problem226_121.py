import math
H,N = map(int,input().split())

print("Yes" if sum(list(map(int,input().split())))>=H else "No")
