N, M = map(int, input().split())

s = []
c = []
for i in range(M):
    x,y = map(int,input().split())
    s.append(x)
    c.append(y)

ans_list = [-1 for i in range(N)]

for i in range(M):
    if ans_list[s[i]-1] != -1 and ans_list[s[i]-1] != c[i]:
        print(-1)
        exit()
    else:
         ans_list[s[i]-1] = c[i]
#print(ans_list)
if ans_list[0] == 0 and N>=2:
    print(-1)
    exit()

ans = 0
for i in range(N):
    if ans_list[i] == -1 and i != 0:
        ans_list[i] = 0
    if ans_list[i] == -1 and i == 0 and N >= 2:
        ans_list[i] = 1
    if ans_list[i] == -1 and i == 0 and N == 1:
        ans_list[i] = 0
    ans += ans_list[i] * (10**(N-i-1))

print(ans)
