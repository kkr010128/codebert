n = input()
ans = 0
for i,j in enumerate(map(int,input().split())):
    ans += (~i&1 and j&1)
print(ans)