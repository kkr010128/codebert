N = list(map(int, input().split(' ')))

sub = N[1] - N[0]
calc = [N[0]]
for i in range(sub):
	calc.append(N[0] + i + 1)
	
count = 0
for i in range(len(calc)):
	if N[2] % calc[i] == 0:
		count += 1
		
print(count)