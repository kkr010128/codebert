a, b, k = map(int, input().split())
ac, k = min(a, k), k - min(a, k)
bc = min(b, k)
print(a-ac, b-bc)