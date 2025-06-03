N,K = map(int,input().split())
li = []
count = 0
for i in range(K):
    d = int(input())
    a = list(map(int,input().split()))
    for j in range(d):
        li.append(a[j])

for i in range(N):
    if i+1 not in li:
        count += 1

print(count)