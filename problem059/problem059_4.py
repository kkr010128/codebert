r_c_str=input().split()
r_c=list(map(lambda i :int(i),r_c_str))
r=r_c[0]
c=r_c[1]
s_str=[input() for i in range(r)]
s_str=[i.split() for i in s_str]
s=[]
for i in s_str:
    s.append(list(map(lambda j :int(j),i)))
for i in range(r):
    s[i].append(sum(s[i]))
s.append([])
for i in range(c+1):
    s[-1].append(0)
for i in range(c):
    for j in range(r):
        s[r][i]+=s[j][i]
s[-1][-1]+=sum(s[r])
for i in s:
    print(*i)
