s = input()
s_reversed = list(reversed(s))
ans = len([(a,b) for a, b in zip(s, s_reversed) if a !=b]) // 2
print(ans)