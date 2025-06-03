import sys
N = int(input())
A = list(map(int,input().split()))

fin = 1
if 0 in A:
    fin = 0
else:
    for i in A:
        fin *= i
        if fin > 10**18:
            print(-1)
            sys.exit()
            
print(fin)