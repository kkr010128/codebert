
N= int(input())
st = [list(map(str,input().split())) for _ in range(N)]
x = input()

ans = 0
flag = False
for s,t in st:
    if flag:
        ans += int(t)
    else:
        if s == x:
            flag = True
print(ans)