s=[]
for i in input().split():
 n=len(s)-1
 if i=='+':s.append(s[n-1]+s[n]);s.pop(n-1);s.pop(n-1)
 elif i=='-':s.append(s[n-1]-s[n]);s.pop(n-1);s.pop(n-1)
 elif i=='*':s.append(s[n-1]*s[n]);s.pop(n-1);s.pop(n-1)
 elif i=='/':s.append(s[n-1]/s[n]);s.pop(n-1);s.pop(n-1)
 else:s.append(int(i))
print(*s)
