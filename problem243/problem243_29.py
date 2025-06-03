n = int(input())
l = []
flag = False
ans = 0

for i in range(n):
    s, t = input().split()
    t = int(t)
    l.append([s, t])

x = input()

for s, t in l:
    if flag == True:
        ans += t
    elif s == x:
        flag = True

print(ans)