import sys
x = int(input())
ans = 2
while(True):
    if x*ans % 360 == 0:
        print(ans)
        sys.exit()
    ans +=1