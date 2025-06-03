n = int(input())

a_list = []
for _ in range(n):
  mini_list = []
  a = int(input())
  for _ in range(a):
    mini_list.append(list(map(int, input().split())))
  a_list.append(mini_list)

ans = 0
for i in range(2**n):
  ans_list = [0]*n
  cnt=0
  while i!=0:
    ans_list[cnt] = i%2
    cnt+=1
    i//=2
  
  flg = True
  for j, syogens in enumerate(a_list):
    if ans_list[j]==0:
      pass
    else:
      for syogen in syogens:
        person = syogen[0]-1
        status = syogen[1]
        if ans_list[person] != status:
          flg=False
  if flg:
    ans = max(ans,sum(ans_list))
print(ans)
