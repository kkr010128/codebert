n = int(input())
tmp = 0
import sys
for i in range(n):
    d = list(map(int,input().split()))
    if d[0] == d[1]:
        tmp += 1
        #check
        if tmp == 3:
            print('Yes')
            sys.exit()
    else:
        tmp = 0
print('No')