# AOJ ALDS1_4_C Dictionary
# Python3 2018.7.3 bal4u

dic = {}
n = int(input())
for i in range(n):
	id, s = input().split()
	if id == "insert": dic[s] = 1
	else: print("yes" if s in dic else "no")
