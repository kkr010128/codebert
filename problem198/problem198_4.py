n=int(input())
s='abcdefghij'
def f(string):
  r=[]
  for i in range(len(string)):
    m=0
    for j in string[i]:
      if ord(j)-97 > m:
        m=ord(j)-97
    for j in range(m+2):
      r.append(string[i] + s[j])
  return r
string=['a']
for i in range(n-1):
  string=f(string)
for a in string:
  print(a)