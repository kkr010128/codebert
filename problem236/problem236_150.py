h = int(input())
w = int(input())
n = int(input())
if h >= w:
    m = h
else:
    m = w
if n%m == 0:
    ans = n//m
else:
    ans = n//m +1
print(ans)