A, B = map(int, input().split())

# floor(1009*0.1)=100 かつ floor(1010*0.1)=101 より、1から1009までの数字を調べればよい
ans = '-1'
for i in range(1010)[::-1]:
  if i*8 // 100 == A and i // 10 == B:
    ans = i

print(ans)
