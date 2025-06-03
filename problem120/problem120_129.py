a = 0
n,k=input().split()
p=input().split(" ")
for i in range(int(n)):
  p[i] = int(p[i])
p=sorted(p)
for i in range(int(k)):
  a += int(p[i])
print(a)