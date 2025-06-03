from sys import stdin,stdout
# n,e=list(map(int,stdin.readline().split()))
n=int(stdin.readline())
for a in range(-400,400):
    for b in range(-400,400):
        if abs(a**5-b**5)==n:
            print(max(a,b),min(a,b))
            exit(0)