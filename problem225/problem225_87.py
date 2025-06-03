H, A = map(int, input().split())
ans = int(H/A)
if (H%A) != 0:
  ans += 1
print(ans)