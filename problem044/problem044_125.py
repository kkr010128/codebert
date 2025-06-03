l=input().split()

a=int(l[0])
b=int(l[1])
c=int(l[2])

def judge(c,n):
    if c%n==0:
        return 1
    else:
        return 0
n=a
result=0
while n<=b:
    result=result+judge(c,n)
    n=n+1

print(result)
