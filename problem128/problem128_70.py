import sys
x,n = map(int,input().split())
p = list(map(int,input().split()))
s = 100
min_i = -1

if x not in p:
    print(x)
    sys.exit()

for i in range(-1,102):
    if i not in p and abs(i-x) < s:
        s = abs(i-x)
        min_i = i

        
print(min_i)
