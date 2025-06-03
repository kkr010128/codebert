#from sys import stdin

#input = stdin.readline
#inputRstrip = stdin.readline().rstrip

#x = input().rstrip()
#n = int(input())

#a,b,c = input().split()
#a,b,c = map(int, input().split())

ST = [input() for i in range(2)]
S = ST[0]
T = ST[1]
ans = len(T)

for i in range(len(S) - len(T) + 1):
	count = len(T)
	for j in range(len(T)):
		if(T[j] == S[i + j]):
			count -= 1
	if(ans > count):
		ans = count
print(ans)