from collections import deque

n = int(input())
x = input()

memo = {0: 0}

def solve(X):
    x = X
    stack = deque([])
    while x:
        if x in memo:
            break
        stack.append(x)
        x = x % bin(x).count("1")
    cnt = memo[x] + 1
    while stack:
        x = stack.pop()
        memo[x] = cnt
        cnt += 1
    return cnt - 1



ans = []
px = x.count("1")

memo1 = [1 % (px - 1)] if px > 1 else []
memo2 = [1 % (px + 1)]
x1 = 0
x2 = 0

for i in range(n):
    if px > 1:
        memo1.append(memo1[-1] * 2 % (px-1))
    memo2.append(memo2[-1] * 2 % (px+1))

for i in range(n):
    if x[-i-1] == '1':
        if px > 1:
            x1 += memo1[i]
            x1 %= (px-1)
        x2 += memo2[i]
        x1 %= (px+1)

for i in range(n):
    if x[-i-1] == "1":
        if px > 1:
            ans.append(solve((x1-memo1[i])%(px-1)) + 1)
        else:
            ans.append(0)
    else:
        ans.append(solve((x2+memo2[i])%(px+1)) + 1)


for ansi in reversed(ans):
    print(ansi)


    

        
