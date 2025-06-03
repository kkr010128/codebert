N = int(input())
A = list(map(int,input().split()))
B = set()

for a in A:
    if a in B:
        print('NO')
        exit()
    else:
        B.add(a)
print('YES')