data = list(map(int, input().split()))
a,b = max(data), min(data)
r = a % b

while r != 0:
    a = b
    b = r
    r = a % b

print(b)