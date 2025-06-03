n = int(input())
a = list(map(int, input().split()))
l = [0] * n

for i in a:
    l[i - 1] += 1
    
for k in range(n):
    print(l[k])