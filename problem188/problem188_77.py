x, y, a, b ,c=map(int,input().split())
p=list(map(int,input().split()))
q=list(map(int,input().split()))
r=list(map(int,input().split()))
sm=0
p.sort()
q.sort()
r.sort(reverse=True)

p=p[(a-x):]
q=q[(b-y):]
p.extend(q)
p.sort()

idx=0
for i in range(len(p)):
    if p[i]>r[idx]:
        break
    else:
        p[i]=r[idx]
        idx+=1
        if c==idx:
            break

print(sum(p))