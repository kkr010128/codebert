n, k = map(int, input().split())
l = [0] * n

for i in range(k):
    d = int(input())
    a = list(map(int, input().split()))
    for j in range(d):
        l[a[j] - 1] += 1
        
count = 0        
for i in range(n):
    if l[i] == 0:
        count += 1
print(count)