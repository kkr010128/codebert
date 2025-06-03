a = list(map(int,input().split()))
ans = "unsafe" if a[1]>=a[0] else "safe"
print(ans)