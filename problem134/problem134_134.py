
N=int(input())
A_list=sorted(list(map(int, input().split())), reverse=True)
ans=1

if 0 in A_list:
  print(0)
  exit()
else:
  for a in A_list:
    ans*=a
    if ans>1e+18:
      print(-1)
      exit()
  print(ans)








