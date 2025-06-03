n,k = map(int,input().split())
l = list(map(int,input().split()))
l.sort()
cnt = 0
s = 0
while(cnt < k):
    s = s+l[cnt]
    cnt = cnt+1

print(s)
