D = int(input())
c = list(map(int, input().split()))
s = []
for k in range(D):
    s.append(list(map(int, input().split())))

ans = 0


scheduled = [0 for _ in range(26)]

for k in range(D):
    t = int(input())
    scheduled[t-1] = -1
    for j in range(26):
        scheduled[j] +=1
        ans -= c[j]*scheduled[j]
    ans += s[k][t-1]
    

    print(ans)