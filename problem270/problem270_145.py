a = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
a = a * 2
c = 0
z = input()
for i in range(0,7):
	if z == a[i]:
		for j in range(i + 1, 14):
			if a[j] == "SUN":
				print(j - i )
