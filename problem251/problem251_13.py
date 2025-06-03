n,k = map(int,input().split())

r,s,p = map(int,input().split())

t = input()
l = [[] for i in range(k)]

ans = 0

for i in range(n):
    mod = i%k
    l[mod].append(t[i])
        
for i in range(k):
    h = ""
    for j in l[i]:
        if j == "r" and h != "p":
            ans += p
            h = "p"
        elif j == "s" and h != "r":
            ans += r
            h = "r"
        elif j == "p" and h != "s":
            ans += s
            h = "s"
        else:
            h = ""
print(ans)    