from math import atan, degrees

def is_divisible(a):
	return 'Yes' if any(int(a/x) == a/x and a/x <= 9 for x in range(1,10)) and a <= 81 else 'No'
	
print(is_divisible(int(input())))