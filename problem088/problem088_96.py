N = int(input())
A = list(map(int, input().split()))

s = 0
height = 0
for a in A:
    height = max(height, a)
    s += height - a
print(s)