from collections import Counter
N = int(input())
A = list(map(int, input().split()))
l =[]
r =[]
for id,h in enumerate(A,start=1):
    r.append(id -h)
    l.append(id +h)

r_cou =Counter(r)
l_cou =Counter(l)
ans =[]
for i in l_cou.keys():
    ans.append(l_cou[i] *r_cou.get(i,0))

print(sum(ans))