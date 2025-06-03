def grading(m,f,r):
	mf = m+f
	if mf >= 80:
		grade = 'A'
	elif mf >= 65:
		grade = 'B'
	elif mf >= 50:
		grade = 'C'
	elif mf >= 30:
		grade = 'D'
	else:
		grade = 'F'
	if -1 in [m,f]:
		grade = 'F'
	if grade == 'D' and r >= 50:
		grade = 'C'
	return grade

data = []
while True:
	temp = [int(s) for s in input().split(' ')]
	if temp == [-1,-1,-1]:
		break
	else:
		data.append(temp)

grades = [grading(*points) for points in data]
[print(g) for g in grades]