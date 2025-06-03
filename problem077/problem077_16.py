abcd = list(map(int, input().split()))

max_pro = -float("inf")
for i in range(2):
  for j in range(1,3):
    product = abcd[i] * abcd[-j]
    if max_pro < product:
      max_pro = product

print(max_pro)