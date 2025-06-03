s=input()
n=len(s)
x=s[0:(n-1)//2]
y=s[(n+3)//2-1:n]
if x==x[::-1] and y==y[::-1] and s==s[::-1]:
  print('Yes')
else:
  print('No')
