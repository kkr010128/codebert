from collections import Counter

n = int(input())

if n == 1:
    print(0)
else:
    lis = [i for i in range(n+1)]
    for i in range(2, int(n**0.5) + 1):
        if lis[i] == i:
            lis[i] = i
            for j in range(i**2, n+1, i):
                if lis[j] == j:
                    lis[j] = i
#print(lis)
def bunkai(m):
    ans = []
    now = lis[m]
    cnt = 1
    for i in range(m):
        m = m//lis[m]
        if now == lis[m]:
            cnt += 1
        else:
            ans.append(cnt)
            cnt = 1
            now = lis[m]
        
        if m == 1:
            break
    return ans

ans = 1
for i in range(2,n):
    tmp = 1
    yaku = bunkai(i)
    for i in yaku:
        tmp *= (i +1)
    ans += tmp

print(ans)


