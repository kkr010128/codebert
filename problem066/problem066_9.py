while 1:
 s=input();l=len(s);n=0
 if'-'==s:break
 for _ in range(int(input())):n+=int(input())
 print((s+s)[n%l:][:l])