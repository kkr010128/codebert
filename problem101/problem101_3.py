a,b,c = map(int, input().split())
k = int(input())
for i in range(k):
    if a >= b:
        b *= 2
        continue
    if b >= c:
        c *= 2
        continue
print("Yes" if a < b and b < c else "No")
