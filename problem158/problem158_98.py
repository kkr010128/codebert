k = int(input())
ab = input().split()
a = int(ab[0])
b = int(ab[1])
l = 0
ans = 0

while l < a:
    l += k

while l <= b:
    ans += 1
    l += k

if ans == 0:
    print("NG")
else:
    print("OK")