import sys
N,K = map(int,input().split())
array_hight = list(map(int,input().split()))

if not ( 1 <= N <= 10**5 and 1 <= K <= 500 ): sys.exit()

count = 0
for I in array_hight:
    if not ( 1 <= I <= 500): sys.exit()
    if I >= K:
        count += 1
print(count)