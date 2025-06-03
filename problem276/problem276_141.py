def ii():return int(input())
def iim():return map(int,input().split())
def iil():return list(map(int,input().split()))
def ism():return map(str,input().split())
def isl():return list(map(str,input().split()))

n = ii()
A = iil()
sA = sum(A)
ans = float('inf')
l = [A[0]]
for i in A[1::]:
    l.append(l[-1]+i)
    if sA < 2*l[-1]:
        print(min(abs(sA-2*l[-1]),abs(sA-2*l[-2])))
        exit()