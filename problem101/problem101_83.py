import sys
a,b,c = map(int,input().split())
k = int(input())
for i in range(k+1):
    if b * 2**i > a:
        n = i
        break
for j in range(k-n+1):
    if c * 2**j > b * 2**n:
        print("Yes")
        sys.exit()
print("No")