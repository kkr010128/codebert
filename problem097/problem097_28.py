import sys

k = int(input())

ans = [0]*(k+1)
ans[0] = 7 % k

if ans[0] == 0:
    print(1)
    
else:
    for i in range(k):
        ans[i+1] = (ans[i]*10 + 7) % k
        
        if ans[i+1] == 0:
            print(i+2)
            sys.exit()
            
    print(-1)