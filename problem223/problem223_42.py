import itertools

n, k = map(int, input().split())
lis = list(map(int,input().split()))

exlis = []


for i in lis:
    a = (1+i)/2
    exlis.append(a)


nlis = list(itertools.accumulate(exlis))


ans  = nlis[k-1]
for j in range(n-k):
    tmp = nlis[j+k] - nlis[j]
    ans = max(ans, tmp)

print(ans)