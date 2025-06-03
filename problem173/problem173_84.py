n = int(input())

sum = (1 + n) * n // 2

sho_3 = n // 3
sho_5 = n // 5
sho_15 = n // 15

s_3 = (sho_3 * 3 + 3) * sho_3 // 2
s_5 = (sho_5 * 5 + 5) * sho_5 // 2
s_15 = (sho_15 * 15 + 15) * sho_15 // 2


print(sum - s_3 - s_5 + s_15)
