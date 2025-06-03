import sys
N,M = map(int,input().split())
array = list(map(int,input().split()))

if not ( 1 <= M <= 100 and M <= N <= 100 ): sys.exit()
if not (len(array) == len(set(array))): sys.exit()

count = 0
standard = sum(array) * (1/(4*M))
for I in array:
    if I >= standard:
        count += 1
print('Yes') if count >= M else print('No')