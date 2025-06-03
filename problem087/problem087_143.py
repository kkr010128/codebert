n = list(map(int, list(input())))

n_sum = sum(n)

print("Yes" if n_sum % 9 == 0 else "No")