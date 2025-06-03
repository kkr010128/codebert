import sys
input = sys.stdin.readline

N = int(input())
d = list(map(int,input().split()))
counter = 0
for i in range(N-1):
    for j in range(i+1,N):
        counter += d[i]*d[j]
print(counter)
