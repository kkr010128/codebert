h = int(input())
cnt = -1

while h > 0:
  h //= 2
  cnt += 1

ans = 2**(cnt+1) - 1

print(ans)