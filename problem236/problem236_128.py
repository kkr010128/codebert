h = int(input())
w = int(input())
n = int(input())
ans = n // max(h,w) if n % max(h,w) == 0 else n // max(h,w) + 1
print(ans)