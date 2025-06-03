n, m = map(int, input().split())
s=[]
c=[]
num=[]
for i in range(m):
  S, C = map(int, input().split())
  s.append(S)
  c.append(C)

for i in range(10**(n+1)):
  String=str(i)
  if len(String) == n and all([String[s[j]-1] == str(c[j]) for j in range(m)]):
    print(str(i))
    exit()
print('-1')