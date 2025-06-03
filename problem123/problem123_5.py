N = int(input())
a = list(map(int,input().split()))

sum = 0
for i in a:
    sum = i^sum

for i in a:
    print(sum^i,end=' ')
