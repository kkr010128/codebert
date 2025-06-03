X, N = map(int,input().split())
li = set(list(map(int,input().split())))
li = list(set(range(102)) - li)

li.sort(reverse=True)
n = 102

for i in li:
    m = abs(X - i)
    if m <= n:
        n = m
        k = i
print(k)