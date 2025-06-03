x, n = map(int, input().split())
p = list(map(int, input().split()))
n = list(i for i in range(-1, 110) if i not in p)

diff = 110
ans = 0

for i in n:
    if diff > abs(x-i):
        diff = abs(x-i)
        ans = i
        
print(ans)