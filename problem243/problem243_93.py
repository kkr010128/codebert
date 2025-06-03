n=int(input())
a=[]
for i in range(n):
    s,t=input().split()
    a.append([s,int(t)])
x=input()
sum1=0
for j in range(n):
    if a[j][0]!=x:
        sum1+=a[j][1]
    else:
        sum1+=a[j][1]
        break
sum2=0
for i in range(n):
    sum2+=a[i][1]
print(sum2-sum1)
