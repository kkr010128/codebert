import sys 
K = int(input())
if K%5==0 or K%2==0:
    print("-1")
    sys.exit()

A = 0
for i in range(K):
    A = (10 * A + 7) % K
    if A == 0:
        print(i+1)
        break