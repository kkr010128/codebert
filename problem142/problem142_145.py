N = input()
N = N[::-1]
a = int(N[0])
ans = []
if a==2 or a==4 or a==5 or a==7 or a==9:
  ans = "hon"
if a==0 or a==1 or a==6 or a==8:
  ans = "pon"
if a==3:
  ans = "bon"
  
print(ans)
