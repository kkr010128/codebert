n,m = map(int,input().split())

s = input()

ans = []
p = n

flag = 1
while flag:
    for j in range(m,0,-1):
        if p-j<=0:
            ans.append(p)
            flag = 0
            break
        elif s[p-j]=='0':
            ans.append(j)
            p-=j
            break
        elif j == 1:
            ans.append(-1)
            flag = 0
            break

print(' '.join(map(str,reversed(ans))) if ans[-1]!=-1 else -1)
