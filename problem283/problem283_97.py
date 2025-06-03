# A - Sum of Two Integers
N = int(input())

if N % 2 == 1:
	N += 1
	
print(int(N / 2 - 1))