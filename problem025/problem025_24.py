n = int(input())
A = list(map(int, input().rstrip().split(" ")))

q = int(input())
M = list(map(int, input().rstrip().split(" ")))

existBits = 1

for a in A:
    existBits |= existBits << a
        
if(__name__ == '__main__'):
    
    for m in M:
        
        judge = (existBits << m)
        
        if(((existBits >> m) & 1) == 1):
            print("yes")
        else:
            print("no")
