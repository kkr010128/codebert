x = int(input())

can = x // 100
need = ((x%100) + 4) // 5

print(1 if can >= need else 0)