n = int(input())
s = ["" for i in range(n)]
t = [0 for i in range(n)]
for i in range(n):
    a, b = input().split()
    s[i], t[i] = a, int(b)
x = input()
ans = 0
flag = False
for i in range(n):
    if s[i] == x:
        flag = True
    elif flag:
        ans += t[i]
print(ans)