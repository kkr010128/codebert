n = int(input())
s = []
t = []
for _ in range(n):
    name,time = map(str,input().split())
    s.append(name)
    t.append(int(time))
target = input()
start = s.index(target)
ans = 0
for i in range(start+1,n):
    ans += t[i]
print(ans)