n, k = map(int, input().split())
listn = list()
for i in range(k):
    d = int(input())
    a = list(map(int, input().split()))
    listn.extend(a)
print(n - len(set(listn)))