n,k = map(int, input().split())
r,s,p = map(int, input().split())
t = input()

def add(x):
    if x == 'r':
        return p
    elif x == 's':
        return r
    else:
        return s

nk =[0]*k
for i in range(n):
    key = i%k
    if nk[key]==0:
        nk[key] = [t[i]]
    else:
        nk[key].append(t[i])
ans = 0
for j in nk:
    if j ==0:
        continue
    ans += add(j[0])
    for k in range(1, len(j)):
        if j[k]== j[k-1]:
            j[k]='q'
        else:
            ans += add(j[k])
print(ans)