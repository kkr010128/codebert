from collections import Counter

X,Y,A,B,C=map(int,input().split())
#3logN
p=list(map(int,input().split()))
q=list(map(int,input().split()))
r=list(map(int,input().split()))
p.sort()
q.sort()
p_list=p[-X:]
q_list=q[-Y:]
r.extend(p_list)
r.extend(q_list)
r.sort()
print(sum(r[-(X+Y):]))