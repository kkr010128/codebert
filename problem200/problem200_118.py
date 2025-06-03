a, b, m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
li = [list(map(int,input().split())) for i in range(m)]
kouho = [min(a)+min(b)]

for l in li:
    kouho.append(a[l[0]-1] + b[l[1]-1] -l[2])

print(min(kouho))