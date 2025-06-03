import itertools

n = int(input())
A = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))

ANS = set()
for i in range(1,n+1):
    A_pairs = list(itertools.combinations(A, i))
    for j in range(len(A_pairs)):
        ANS.add(sum(A_pairs[j]))

for i in range(q):
    if m[i] in ANS:
        print('yes')
    else:
        print('no')
