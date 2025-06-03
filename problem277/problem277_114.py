h,w,k = list(map(int, input().split()))
s = [input() for _ in range(h)]

strawberry = []

for i in s:
    if '#' in i:
        strawberry.append(True)
    else: strawberry.append(False)
ans = [[0]*w for _ in range(h)]

num = 0
for i in range(h):
    flag = 0
    if strawberry[i]:
        num += 1
        for j in range(w):
            if s[i][j]=='#':
                flag += 1
            if flag==2:
                num += 1
                flag = 1
            ans[i][j] = num

tmp = strawberry.index(True)
for i in range(h):
    if strawberry[i]==False:
        ans[i] = ans[tmp]
    else:
        tmp = i

for i in ans:
    print(' '.join(map(str,i)))
