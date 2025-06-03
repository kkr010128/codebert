n = int(input())
*X, = map(int, input().split())
m = int(input())
*Y, = map(int, input().split())
 
bits = 1
for a in X:
    bits |= bits << a
 
for m in Y:
    print("yes"*((bits >> m) & 1)or"no")
