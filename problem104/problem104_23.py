import sys
L,R,d = map(int, sys.stdin.readline().split())
# L=5
# R=10
# d=2
result = 0
for index in range(L,R+1):
    if index % d == 0:
        result += 1
        
print(result)
        

