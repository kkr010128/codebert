N,M = map(int,input().split())


ans = []
s = 1
e = M+1
while e>s:
    ans.append([s,e])
    s += 1
    e -= 1

s = M+2
e = 2*M+1
while e>s:
    ans.append([s,e])
    s += 1
    e -= 1

for s,e in ans:
    print(s,e)
    
