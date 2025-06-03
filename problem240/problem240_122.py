n, m = [int(i) for i in input().split()]
lst_pena = [[False, 0] for i in range(n)]
cnt_pena = 0
cnt_ca = 0
for i in range(m):
	n, m = [j for j in input().split()]
	n = int(n) - 1
	if lst_pena[n][0] == False and m == 'AC':
		lst_pena[n][0] = True
		cnt_ca += 1
	elif lst_pena[n][0] == False and m == 'WA':
		lst_pena[n][1] += 1
sum_pena = sum([i[1] if i[0] else 0 for i in lst_pena])
print(f'{cnt_ca} {sum_pena}')