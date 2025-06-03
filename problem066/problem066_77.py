while 1:
 s=input()
 if'-'==s:break
 for _ in range(int(input())):
  a=int(input())
  s=s[a:]+s[:a]
 print(s)