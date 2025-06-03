'''
INPUT SHORTCUTS
N, K = map(int,input().split())
N ,A,B = map(int,input().split())
string = str(input())
arr = list(map(int,input().split()))
N = int(input())
'''
n , m = map(int,input().split())
if n>=10:
	print(m)
else:
	m = m + (100*(10-n))
	print(m)