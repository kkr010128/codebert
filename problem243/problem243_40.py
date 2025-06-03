n=int(input())
l=[input().split() for i in range(n)]
x=input()
time=0
for i in range(n):
    time += int(l[i][1])
    if l[i][0]==x:
        time=0


print(time)