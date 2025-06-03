n=int(input())
s=list(map(str,input()))
if n%2==0:
    num=int(n/2)
    Sx=s[0:num]
    Sy=s[num:n]
    if Sx==Sy:
      print("Yes")
    else:
      print("No")
else:
  print("No")