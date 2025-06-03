A, B = input().split()
B = B.replace('.', '')

A, B = list(map(int, [A, B]))

ans_b = A*B

print(int(ans_b//100))
