import sys
N = int(input())
lsA = list(map(int,input().split()))
for i in range(N):
    if lsA[i] % 2 == 0:
        if lsA[i] % 3 == 0 or lsA[i] % 5 == 0:
            continue
        else:
            print('DENIED')
            sys.exit()
print('APPROVED')