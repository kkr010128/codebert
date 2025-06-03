A, B = map(int, input().split())

s = add = max(A, B)
while True:
    if s % A == 0 and s % B == 0:
        break
    s += add

print(s)