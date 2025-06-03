#template
def inputlist(): return [int(j) for j in input().split()]
def listinput(): return input().split()
#template
N,R = inputlist()
if N >= 10:
    print(R)
else:
    print(R + 100*(10-N))