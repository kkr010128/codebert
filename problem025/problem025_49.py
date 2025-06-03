n = int(input())
A = list(map(int, input().split()))
q = int(input())
B = list(map(int, input().split()))

s = set()
def check(i, m):
    if i == n:
        s.add(m)
        return
    check(i+1, m+A[i])
    check(i+1, m)

check(0,0)

for i in B:
    if i in s:
        print('yes')
    else:
        print('no')
