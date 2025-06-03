n = int(input())
x = list(map(int, input().split()))
p = [0] * 100
for i in range(1, 101):
    for j in x:
        p[i-1] += (i - j)**2
print(min(p))