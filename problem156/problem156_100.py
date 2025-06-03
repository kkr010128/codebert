def main():
	X = int(input())
	fifth_power = [x ** 5 for x in range(201)]
	for i in range(len(fifth_power)):
		p = fifth_power[i]
		q1 = abs(X - p)
		q2 = abs(X + p)
		if q1 in fifth_power:
			if p + q1 == X:
				print(fifth_power.index(p), -fifth_power.index(q1))
			elif p - q1 == X:
				print(fifth_power.index(p), fifth_power.index(q1))
			return 0
		if q2 in fifth_power:
			print(fifth_power.index(q2), fifth_power.index(p))
			return 0

main()