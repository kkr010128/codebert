n = input()

ls = list(n)

wa = 0
for i in range(len(ls)):
    wa += int(ls[i])


print('Yes') if wa % 9 == 0 else print('No')