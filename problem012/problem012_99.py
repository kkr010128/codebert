import math

N = int(input())
ans = 0

def solve(x):
    if x==2:
        return 1
    elif x%2==0:
        return 0
    else:
        for i in range(3, math.ceil(math.sqrt(x)) + 1, 2):
            if x%i ==0:
                return 0
        return 1
for i in range(N):
    if solve(int(input())) ==1:
        ans +=1
print(ans)