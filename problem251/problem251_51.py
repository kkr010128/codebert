n, k = map(int,input().split())
r,s,p = map(int,input().split())
t = list(input())

ans = 0
for i in range(len(t)):
    tmp = t[i]
    if i >= k:
        if tmp == t[i-k]:
            t[i] = "c"
            continue
    if tmp == "r":
        ans += p
    elif tmp == "s":
        ans += r
    elif tmp == "p":
        ans += s
        
print(ans)