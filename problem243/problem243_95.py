n=int(input())
s=[0]*n
t=[0]*n
for i in range(n):
    s[i],t[i]=input().split()
    t[i]=int(t[i])
print(sum(t[s.index(input())+1:]))