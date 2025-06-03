s=input()
for _ in range(int(input())):
 a=input().split()
 if a[0][0]=='p':print(s[int(a[1]):int(a[2])+1])
 else:
  t=a[3]if'p'==a[0][2]else s[int(a[1]):int(a[2])+1][::-1]
  s=s[0:int(a[1])]+t+s[int(a[2])+1:]