n = input()
a = list(map(int, input().split()))
max = 0
step = 0            
for i in a:
	if max > i:
		step += max - i
	else:
		max = i

print(step) 