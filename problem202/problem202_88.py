#26
N,A,B = map(int,input().split())
num = int(N/(A+B))
blue = 0

blue = num*A
if (N-num*(A+B)) <= A:
    blue += (N-num*(A+B))
else:
    blue += A

print(blue)