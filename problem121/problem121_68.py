n=int(input())
p=1
while n > 0:
  n-=26**p
  p+=1
else:
  p-=1
  if n==0:
    ans="z"*p
    print(ans)
  else:
    n+=26**p
    num=[]
    for i in range(1,p+1):
      if n%(26**(p-i))==0:
        a=int(n/(26**(p-i)))-1
        q=p-i
        num.append(a)
        break
      else:
        a=n//(26**(p-i))
        num.append(a)
        n-=a*(26**(p-i))
    al=[]
    if n==0:
      for i in range(p-1):
        m=chr(97+num[i])
        al.append(m)
      al.append(chr(96+num[p-1]))
      ans=''.join(al)
    else:
      for i in num:
        m=chr(97+i)
        al.append(m)
      al.append("z"*q)
      ans=''.join(al)
    print(ans)