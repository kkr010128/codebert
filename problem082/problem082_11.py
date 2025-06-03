s=input()
t=input()
a = len(s)
b = len(t)
l = []
for i in range(a-b+1):
    cnt = 0
    c = s[i:i+b]
    for x, y in zip(c, t):
        if x != y:
            cnt +=1
    l.append(cnt)
print(min(l))