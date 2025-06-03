N = int(input())
name=[""]*N
time=[0]*N
for i in range(N):
  a=input()
  name[i]=a.split()[0]
  time[i]=int(a.split()[1])
print(sum(time[name.index(input())+1:]))