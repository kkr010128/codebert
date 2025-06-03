import sys

N,K = map(int,input().split())
H = sorted(list(map(int,input().split())),reverse = True)

for i in range(N):
    if not H[i] >= K:
        print(i)
        sys.exit()
        
print(N)