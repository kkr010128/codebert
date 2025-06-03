import sys
input = sys.stdin.readline
 
############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))#might need to remove the -1
def invr():
    return(map(int,input().split()))

d, t, s = invr()

if d/s<=t:
	print('Yes')
else:
	print('No')