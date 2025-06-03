a = input()
N = len(a)
c = []
temp = int(1)
ans = int(0)
for i in range(N):
    if i != N-1:
      if a[i] == a[i+1]:
        temp += 1
      else:
        c.append(temp)
        temp = 1
    else:
      if a[i-1] == a[i]:
        c.append(temp)
      else:
        c.append(1)

clen = len(c)

if a[0] == "<" and clen % 2 == 1:
    c.append(0)
elif a[0] == ">" and clen % 2 == 0:
    c.append(0)

if a[0] == "<":
    for i in range(0,clen,2):
        maxi = max([c[i],c[i+1]])
        mini = min([c[i],c[i+1]])
        ans += maxi*(maxi+1)/2
        ans += mini*(mini-1)/2
else:
    ans += c[0]*(c[0]+1)/2
    for i in range(1,clen,2):
        maxi = max([c[i],c[i+1]])
        mini = min([c[i],c[i+1]])
        ans += maxi*(maxi+1)/2
        ans += mini*(mini-1)/2
    
print(int(ans))