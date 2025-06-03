#pdf見た
n = int(input())
xl = [list(map(int,input().split())) for i in range(n)]
sf = []
choice = -1e+9
for x,l in xl:
    sf.append([x-l,x+l])
sf.sort(key=lambda x:x[1])
cnt = 0
for s,f in sf:
    if choice <= s:
        cnt += 1
        choice = f
        
print(cnt)