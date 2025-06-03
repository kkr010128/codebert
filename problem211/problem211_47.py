i = input()
N, R = map(int, i.split())

if N >= 10: print(R) 
else: print(R + 100 * (10-N))