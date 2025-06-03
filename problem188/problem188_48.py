x,y,a,b,c = map(int,input().split())
p = list(map(int,input().split()))
q = list(map(int,input().split()))
r = list(map(int,input().split()))

p = sorted(p,reverse=True)
q = sorted(q,reverse=True)
r = sorted(r,reverse=True)

lis = p[:x]
lis.extend(q[:y])

lis = sorted(lis)

#print(lis)
ans = []
lr = len(r)
for i in range(len(lis)):
    if i<lr:
        ans.append(max(lis[i],r[i]))
    else:
        ans.append(lis[i])

print(sum(ans))
