N = int(input())
S = list(input())

ans = []

for s in S:
  ord_plus = ord(s)+N
  if ord_plus > 90:
    ord_plus -= 26
  ans.append(chr(ord_plus))
print("".join(ans))