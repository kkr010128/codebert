import sys 

buildings = tuple(i for i in range(4)) 
floors = tuple(i for i in range(3)) 
rooms = tuple(i for i in range(10)) 
occupant = [[[0 for r in rooms] for f in floors] for b in buildings] 

n = input()  

for line in sys.stdin: 
	b, f, r, v = map(int, line.split()) 
	occupant[b - 1][f - 1][r - 1] += v 

for b in buildings: 
	if b: 
		print('####################') 
	for f in floors: 
		print("", *occupant[b][f])
