n=int(input())
a=[]
b=[0]*n
t_sum=0
for i in range(n):
    s,t=input().split()
    tt=int(t)
    t_sum+=tt
    a.append(s)
    b[i]=t_sum
x=input()
print(t_sum-b[a.index(x)])