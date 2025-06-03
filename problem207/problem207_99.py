# B - Bingo
A = [0]*101
for i in range(3):
    tmp = list(map(int,input().split()))
    for j in range(3):
        A[tmp[j]] = 3*i+j+1
N = int(input())
S = set()
for _ in range(N):
    b = int(input())
    S.add(A[b])

def bingo(l):
    ans = False
    for x,y,z in l:
        if x in S and y in S and z in S:
            ans = True
            break
    return ans

if bingo([(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]):
    print('Yes')
else:
    print('No')