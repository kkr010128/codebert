n=int(input())
now=0
for i in range(1,n+1):
    now+=(i+(i*(n//i)))*(n//i)//2
print(now)