import itertools

n = int(input())
a = list(map(int,input().split()))
q = int(input())
m = list(map(int,input().split()))

data = []
for i in itertools.product(range(2),repeat=n):
    data.append(sum([i[j]*a[j] for j in range(n)]))
    
for i in m:
    if i in data:
        print("yes")
    else:
        print("no")
