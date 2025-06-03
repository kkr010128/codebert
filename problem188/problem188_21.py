X,Y,A,B,C=map(int,input().split())
ls_a=sorted(list(map(int,input().split())))
ls_b=sorted(list(map(int,input().split())))
ls_c=sorted(list(map(int,input().split())))
ls_x=ls_a[A-X:A]
ls_y=ls_b[B-Y:B]
ls_c.reverse()

ans=sum(ls_x)+sum(ls_y)
a=b=c=0
for _ in range(min([X+Y,C])):
  if a==len(ls_x):
    m=min([ls_y[b],ls_c[c]])
    if m==ls_y[b]:
      ans+=(-ls_y[b]+ls_c[c])
      b+=1
      c+=1
    else:
      break
  elif b==len(ls_y):
    m=min([ls_x[a],ls_c[c]])
    if m==ls_x[a]:
      ans+=(-ls_x[a]+ls_c[c])
      a+=1
      c+=1
    else:
      break
  else:    
    m=min([ls_x[a],ls_y[b],ls_c[c]])
    if m==ls_x[a]:
      ans+=(-ls_x[a]+ls_c[c])
      a+=1
      c+=1
    elif m==ls_y[b]:
      ans+=(-ls_y[b]+ls_c[c])
      b+=1
      c+=1
    else:
      break
print(ans)