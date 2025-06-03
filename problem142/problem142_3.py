N = input()
if len(N) == 1:
	if N == '3':
		print('bon')
	elif N == '0' or N == '1' or N == '6' or N == '8':
		print('pon')
	else:
		print('hon')
elif len(N) == 2:
	if N[1] == '3':
		print('bon')
	elif N[1] == '0' or N[1] == '1' or N[1] == '6' or N[1] == '8':
		print('pon')
	else:
		print('hon')
elif len(N) == 3:
	if N[2] == '3':
		print('bon')
	elif N[2] == '0' or N[2] == '1' or N[2] == '6' or N[2] == '8':
		print('pon')
	else:
		print('hon')