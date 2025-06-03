import statistics

n=int(input())
x=list(map(int,input().split()))
p1 = int(statistics.mean(x))
p2=p1+1
s1=0
s2=0
for i in range(n):
    s1+=(x[i]-p1)**2
    s2+=(x[i]-p2)**2
print(min(s1,s2))
