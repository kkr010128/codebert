X, N = [int(i) for i in input().split()]
P = [int(i) for i in input().split()]
# Xは0~101の値になる
result = 0
current = 102
for i in range(102):
    if i not in P:
        if abs(X - i) < current:
            result = i
            current = abs(X - i)
print(result)