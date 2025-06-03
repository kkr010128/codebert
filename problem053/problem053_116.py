n = int(input())
a = list(map(int, input().split()))
a = a[::-1]
for cnt, item in enumerate(a, 1):
    if cnt == n:
        print(item)
    else:
        print(item,end=' ')