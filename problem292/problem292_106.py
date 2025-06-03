n = int(input())
l = list(map(int,input().split(' ')))
x = 0
start = 1

for i in l:
    for j in range(start,n):
        x += (i*l[j])
    start += 1

print(x)