N = int(input())
A = list(map(int, input().split()))
se = set()
for i in range(1<<N):
    tot = 0
    for j in range(N):
        if i&(1<<j): tot += A[j]
    se.add(tot)
_ = int(input())
Q = list(map(int, input().split()))
for q in Q:
    if q in se:
        print("yes")
    else:
        print("no")

