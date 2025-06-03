N,M,K = map(int,input().split())
a=list(map(int, input().split()))
b=list(map(int, input().split()))
a.insert(0,0)
b.insert(0,0)
b_num = sum(b)
b_best = M
j = M
a_num = 0
maxmize = 0
num = 0
for i in range(N+1):
  a_num +=a[i]
  flag = 1
  while flag == 1:
    num = b_num+a_num
    if num<=K:
      maxmize = max(M+i,maxmize)
      break
    else:
      if  not b:
        break
      else:
        j = b.pop()
        M-=1
        b_num = b_num-j
print(maxmize)    