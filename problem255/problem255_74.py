n = int(input())
a, b = map(list, input().split())

if len(a) == len(b):
    for i in range(0, len(a)):
        print(a[i] + b[i], end = "")