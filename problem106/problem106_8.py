import math
N = int(input())

ans = [0] * N
n = int(math.sqrt(N)) 

for x in range(1, n+1):
    for y in range(1, x+1):
        for z in range(1, y+1):
            i = x**2 + y**2 + z**2 + x*y + y*z + z*x
            if i <= N:
                if x == y == z:
                    ans[i-1] += 1
                elif x == y or y == z:
                    ans[i-1] += 3
                else:
                    ans[i-1] += 6

for j in range(N):
    print(ans[j])