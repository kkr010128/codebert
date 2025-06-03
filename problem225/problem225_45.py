# Serval vs Monster
H, A = map(int, input().split())
ans = (H // A) + min(1, H % A)
print(ans)