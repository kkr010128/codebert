def top(n):
    return int(str(n)[0])

def bottom(n):
    return int(str(n)[-1])

n = int(input())
c = [[0 for _ in range(10)] for _ in range(10)]

for i in range(1,n+1):
    c[top(i)][bottom(i)] += 1
ans = 0
for i in range(10):
    for j in range(10):
        ans += c[i][j]*c[j][i]
print(ans)