a, b = list(map(int, input().split()))
s = sum(list(map(int, input().split())))
print(max(a-s, -1))
