N = int(input())
x = []
for i in range(N):
    s, t = input().split()
    x.append([s, int(t)])

X = input()

count = False
ans = 0
for i in range(N):
    if count:
        ans += x[i][1]
    if x[i][0] == X:
        count = True

print(ans)
