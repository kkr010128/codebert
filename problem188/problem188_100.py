X, Y, A, B, C = list(map(int,input().split()))
p = list(map(int,input().split()))
q = list(map(int,input().split()))
r = list(map(int,input().split()))
 
p.sort(reverse=True)
q.sort(reverse=True)
r.sort(reverse=True)
 
p.append(float("inf"))
q.append(float("inf")) 

Z = 0
while Z < C:
  if min(p[X - 1], q[Y - 1]) < r[Z]:
    if p[X - 1] < q[Y - 1]:
      X -= 1
      Z += 1
    else:
      Y -= 1
      Z += 1
    continue
  break
 
print(sum(p[:X]) + sum(q[:Y]) + sum(r[:Z]))